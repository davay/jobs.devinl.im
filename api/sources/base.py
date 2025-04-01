from typing import List

from sqlmodel import SQLModel


class CategorySource(SQLModel):
    name: str
    url: str


class CompanySource(SQLModel):
    name: str
    categories: List[CategorySource]
