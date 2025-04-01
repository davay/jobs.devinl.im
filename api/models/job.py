from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from category import Category


class Job(SQLModel, table=True):
    __tablename__ = "job"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    category_id: int | None = Field(
        default=None, foreign_key="category.id", ondelete="CASCADE"
    )
    title: str = Field(index=True)
    date: datetime | None = Field(default=None)
    category: Optional["Category"] = Relationship(back_populates="jobs")
