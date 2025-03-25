from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from company import Company


class Category(SQLModel, table=True):
    __tablename__ = "category"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    company_id: int | None = Field(
        default=None, foreign_key="company.id", ondelete="CASCADE"
    )
    name: str = Field(index=True)
    url: str
    company: Optional["Company"] = Relationship(back_populates="categories")
