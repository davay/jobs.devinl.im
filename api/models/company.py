from sqlmodel import Field, SQLModel


class Company(SQLModel, table=True):
    __tablename__ = "company"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    url: str
