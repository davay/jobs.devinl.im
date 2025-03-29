from sqlmodel import SQLModel


class SourceDTO(SQLModel):
    company_name: str  # for display
    category_id: int  # to be passed back after scraping
    category_name: str  # for display
    url: str


class JobDTO(SQLModel):
    title: str
    category_id: int
    date: str
    retrieval_date: str
