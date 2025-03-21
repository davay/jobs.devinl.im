## Description

While applying, it's good to apply to recently posted jobs but searching for them manually across multiple sites gets old. 

Sometimes these job sites do let you setup notifications, but even then the implementation is inconsistent.

There are browser extensions that automatically watch for changes, but that still feels clunky. 

There is a site that do this: [JobRadar](https://www.jobradar.live/) but it seems that they're missing a lot of companies and is not user-configurable.

So I want to make a similar site except that users can set their own sites and keywords to monitor, with all configuration data saved locally in caches (export will be allowed).

## Design

![](assets/images/mockup.png)

Next good-to-haves:
- Location filter 
- Browser notification

## System Architecture

![](assets/images/architecture.png)

Design choices:
- User config stored in client (exportable).
- API service handles requests, email/browser notifications, and scraper scheduling
- Postgres stores scraped content, page hash, and scraping history
- Scraper first does a diff detect on page hash. If page has changed, it will use llm-scraper with local ollama to parse.
- Ollama will be used to host SmolLM 1.7B.
- SmolLM should let us scrape more reliably from any website without having to manually configure rules for each site.
