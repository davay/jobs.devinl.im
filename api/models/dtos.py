from datetime import datetime

from sqlmodel import SQLModel


class SourceDTO(SQLModel):
    company_name: str  # for display
    category_id: int  # to be passed back after scraping
    category_name: str  # for display
    url: str

    # notice that this is now a str and no longer a datetime
    last_refreshed: str | None = None


class ScrapedJobDTO(SQLModel):
    title: str
    category_id: int
    date: str


class SubmitJobsResponseDTO(SQLModel):
    created_count: int


class JobSearchParamsDTO(SQLModel):
    keywords: list[str]
    page: int
    limit: int


class JobSearchResultDTO(SQLModel):
    title: str
    company: str
    category: str
    url: str
    date: datetime | None = None
    last_refreshed: str | None = None


class JobSearchResponseDTO(SQLModel):
    results: list[JobSearchResultDTO]
    total_pages: int
