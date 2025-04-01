import asyncio
import json
import os
from datetime import datetime, timedelta
from typing import List

import requests
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CacheMode,
    CrawlerRunConfig,
    LLMConfig,
)
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from pydantic import BaseModel, Field


class Job(BaseModel):
    title: str = Field(..., description="Job title")
    date: str = Field(..., description="Job posting date or last updated date")


async def main():
    api_url = "http://0.0.0.0:8000"
    get_sources_url = f"{api_url}/get_sources"
    submit_jobs_url = f"{api_url}/submit_jobs"
    today = datetime.today().date()
    today_str = today.isoformat()

    pruning_filter = PruningContentFilter()  # type: ignore
    md_generator = DefaultMarkdownGenerator(content_filter=pruning_filter)
    crawler_config = CrawlerRunConfig(  # type: ignore
        markdown_generator=md_generator,
        delay_before_return_html=5,
        word_count_threshold=1,
        wait_until="networkidle",
        cache_mode=CacheMode.BYPASS,
        only_text=True,
        exclude_social_media_links=True,
        extraction_strategy=LLMExtractionStrategy(  # type: ignore
            schema=Job.model_json_schema(),
            extraction_type="schema",
            input_format="fit_markdown",
            llm_config=LLMConfig(
                provider="anthropic/claude-3-5-haiku-latest",
                api_token=os.environ.get("ANTHROPIC_API_KEY"),
            ),
            instruction=f"""Extract from each job posting:
            1. Job Title: The exact title as shown (e.g., "Director, Cloud Platform - Seattle, WA")
            2. Date: The job posting date or last updated date in YYYY-MM-DD format.
               - For "Today" use "{today_str}"
               - For "Yesterday" use "{(today - timedelta(days=1)).isoformat()}"
               - For "X days ago" calculate from current date

            Use "N/A" for any missing information.
            """,
        ),
    )

    get_sources_response = requests.get(get_sources_url)
    sources = get_sources_response.json()

    browser_config = BrowserConfig(browser_type="firefox", headless=True, verbose=True)  # type: ignore
    async with AsyncWebCrawler(config=browser_config) as crawler:  # type: ignore
        for source in sources:
            jobs = []
            result = await crawler.arun(
                url=source["url"],
                config=crawler_config,
            )

            ### FOR TESTING ###
            # with open("raw_html.txt", "w") as file:
            #     file.write(result.html)
            # with open("cleaned_html.txt", "w") as file:
            #     file.write(result.cleaned_html)
            #
            # markdown = result.markdown
            # with open("raw_markdown.txt", "w") as file:
            #     file.write(markdown.raw_markdown)
            # with open("filtered_markdown.txt", "w") as file:
            #     file.write(markdown.fit_markdown)
            # with open("filtered_html.txt", "w") as file:
            #     file.write(markdown.fit_html)
            # with open("result.txt", "w") as file:
            #     file.write(result.extracted_content)

            contents: List(dict) = json.loads(result.extracted_content)  # type: ignore
            for content in contents:
                job = {}
                job["title"] = content["title"]
                job["category_id"] = int(source["category_id"])
                job["date"] = content["date"]
                job["last_refreshed"] = today_str
                jobs.append(job)

            requests.post(url=submit_jobs_url, json=jobs)


if __name__ == "__main__":
    asyncio.run(main())
