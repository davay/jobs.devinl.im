from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from category import Category


class Company(SQLModel, table=True):
    __tablename__ = "company"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    categories: list["Category"] = Relationship(back_populates="company")
