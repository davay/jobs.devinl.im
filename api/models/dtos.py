from sqlmodel import SQLModel


class SourceDTO(SQLModel):
    company_name: str  # for display
    category_id: int  # to be passed back after scraping
    category_name: str  # for display
    url: str


class ScrapedJobDTO(SQLModel):
    title: str
    category_id: int
    date: str
    retrieval_date: str


class JobSearchParamsDTO(SQLModel):
    keywords: list[str]
    page: int
    limit: int


class JobSearchResultDTO(SQLModel):
    title: str
    company: str
    category: str
    url: str
    date: str | None
    retrieval_date: str
