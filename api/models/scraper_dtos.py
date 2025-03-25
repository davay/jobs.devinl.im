from sqlmodel import SQLModel


class SourceDTO(SQLModel):
    company: str
    category: str
    url: str
