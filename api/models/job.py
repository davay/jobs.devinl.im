from datetime import datetime

from sqlmodel import Field, SQLModel


class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    company_id: int | None = Field(
        default=None, foreign_key="company.id", ondelete="CASCADE"
    )
    title: str
    date: datetime | None = None
