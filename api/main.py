import math
import os
from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlmodel import Session, case, col, desc, or_, select

from database import get_engine
from models import (
    Category,
    Job,
    JobSearchParamsDTO,
    JobSearchResponseDTO,
    JobSearchResultDTO,
    ScrapedJobDTO,
    SourceDTO,
    SubmitJobsResponseDTO,
)

is_production = os.getenv("ENVIRONMENT") == "production"

# so that docs work https://fastapi.tiangolo.com/advanced/behind-a-proxy/
root_path = "/api" if is_production else ""

app = FastAPI(root_path=root_path)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = get_engine()


@app.get("/get_sources", response_model=List[SourceDTO])
def get_sources():
    with Session(engine) as session:
        result = []

        statement = select(Category)
        categories = session.exec(statement).all()

        if not categories:
            raise HTTPException(status_code=404, detail="No categories found")

        current_time = datetime.now()
        for category in categories:
            last_refreshed_string = "never"
            if category.last_refreshed:
                last_refreshed_delta = current_time - category.last_refreshed
                hours_ago = int(last_refreshed_delta.total_seconds() / 3600)
                last_refreshed_string = f"{hours_ago} hours ago"

            data = {
                # ignored err, company is guaranteed to exist by design, sqlmodel quirk forces optional type in definition
                "company_name": category.company.name,  # type: ignore
                "category_id": category.id,
                "category_name": category.name,
                "url": category.url,
                "last_refreshed": last_refreshed_string,
            }
            result.append(data)

        return result


@app.post("/submit_jobs", response_model=SubmitJobsResponseDTO)
def submit_jobs(jobs: list[ScrapedJobDTO], first_batch: bool = False):
    with Session(engine) as session:
        submit_jobs_response = SubmitJobsResponseDTO(created_count=0)

        if first_batch:
            session.delete(Job)
            session.commit()

        updated_categories = set()

        for job in jobs:
            cleaned_date = None
            if job.date and job.date != "None":
                cleaned_date = datetime.fromisoformat(job.date)

            new_job = Job(
                title=job.title,
                category_id=job.category_id,
                date=cleaned_date,
            )
            session.add(new_job)
            submit_jobs_response.created_count += 1
            updated_categories.add(job.category_id)

        # update each category's last_refreshed date only once
        current_time = datetime.now()
        for category_id in updated_categories:
            category = session.get(Category, category_id)
            if category:
                category.last_refreshed = current_time

        session.commit()
        return submit_jobs_response


@app.post("/search_jobs", response_model=JobSearchResponseDTO)
def search_jobs(search_params: JobSearchParamsDTO):
    with Session(engine) as session:
        results = []

        statement = select(Job).order_by(desc(Job.date))

        if search_params.keywords:
            keyword_conditions = [
                col(Job.title).ilike(f"%{keyword.strip()}%")
                for keyword in search_params.keywords
            ]
            statement = statement.where(or_(*keyword_conditions))

        count_query = select(func.count()).select_from(statement.subquery())
        total_count = session.scalar(count_query)

        total_pages = 1
        if total_count:
            total_pages = math.ceil(total_count / search_params.limit)

        statement = statement.offset(search_params.page * search_params.limit).limit(
            search_params.limit
        )

        jobs = session.exec(statement).all()

        if not jobs:
            raise HTTPException(status_code=404, detail="No jobs found")

        current_time = datetime.now()
        for job in jobs:
            last_refreshed_delta = current_time - job.category.last_refreshed  # type: ignore
            hours_ago = int(last_refreshed_delta.total_seconds() / 3600)

            jobSearchResult = JobSearchResultDTO(
                title=job.title,
                company=job.category.company.name,  # type: ignore
                category=job.category.name,  # type: ignore
                url=job.category.url,  # type: ignore
                date=job.date,
                last_refreshed=f"{hours_ago} hours ago",
            )
            results.append(jobSearchResult)

        jobSearchResponse = JobSearchResponseDTO(
            results=results, total_pages=total_pages
        )

        return jobSearchResponse
