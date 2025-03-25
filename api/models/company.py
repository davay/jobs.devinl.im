from sqlmodel import Field, SQLModel


class Company(SQLModel, table=True):
    __tablename__ = "company"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
