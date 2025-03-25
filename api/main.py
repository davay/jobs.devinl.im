from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from database import get_engine, reset_database, seed_database
from models import Category

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = get_engine()
reset_database(engine)
seed_database(engine)


@app.get("/get_sources")
def get_sources():
    with Session(engine) as session:
        result = []
        statement = select(Category)

        categories = session.exec(statement).all()

        if not categories:
            raise HTTPException(status_code=404, detail="No categories found")

        for category in categories:
            data = {
                # ignored err, company is guaranteed to exist by design, sqlmodel quirk forces optional type in definition
                "company": category.company.name,  # type: ignore
                "category": category.name,
                "url": category.url,
            }
            result.append(data)

        return result
