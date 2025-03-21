import { chromium } from 'playwright';
import { z } from 'zod';
import { ollama } from 'ollama-ai-provider';
import LLMScraper from 'llm-scraper';

async function main() {
  // Launch a browser instance
  const browser = await chromium.launch();

  try {
    // Initialize LLM provider
    const llm = ollama('smollm2:1.7b');

    // Create a new LLMScraper
    const scraper = new LLMScraper(llm);

    // Open new page
    const page = await browser.newPage();
    await page.goto('https://news.ycombinator.com');

    // Define schema to extract contents into
    const schema = z.object({
      top: z
        .array(
          z.object({
            title: z.string(),
            points: z.number(),
            by: z.string(),
            commentsURL: z.string(),
          })
        )
        .length(5)
        .describe('Top 5 stories on Hacker News'),
    });

    // Run the scraper
    const { data } = await scraper.run(page, schema, {
      format: 'html',
    });

    // Show the result from LLM
    console.log(data.top);

    await page.close();
  } catch (error) {
    console.error('Error running scraper:', error);
  } finally {
    await browser.close();
  }
}

main().catch(console.error);
