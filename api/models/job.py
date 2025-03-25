from datetime import datetime

from sqlmodel import Field, SQLModel


class Job(SQLModel, table=True):
    __tablename__ = "job"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    category_id: int | None = Field(
        default=None, foreign_key="category.id", ondelete="CASCADE"
    )
    title: str = Field(index=True)
    date: datetime | None = None
