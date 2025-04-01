from typing import TYPE_CHECKING, Optional
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from company import Company
    from job import Job


class Category(SQLModel, table=True):
    __tablename__ = "category"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    company_id: int | None = Field(
        default=None, foreign_key="company.id", ondelete="CASCADE"
    )
    name: str = Field(index=True)
    url: str
    last_refreshed: datetime | None = Field(default=None)
    company: Optional["Company"] = Relationship(back_populates="categories")
    jobs: list["Job"] = Relationship(back_populates="category")
