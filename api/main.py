import socket
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from database import get_engine, reset_database, seed_database
from models import Category, Job, JobDTO, SourceDTO

hostname = socket.gethostname()
is_production = "jobs.devinl.im" in hostname
root_path = "/api" if is_production else ""

app = FastAPI(root_path=root_path)
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


@app.get("/get_sources", response_model=List[SourceDTO])
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
                "company_name": category.company.name,  # type: ignore
                "category_id": category.id,
                "category_name": category.name,
                "url": category.url,
            }
            result.append(data)

        return result


# TODO: Response model
@app.post("/submit_jobs")
def submit_jobs(jobs: list[JobDTO]):
    with Session(engine) as session:
        results = {"created": [], "skipped": []}
        for job in jobs:
            # statement = select(Job).where(Job.category.company.id == job.company_id)  # type: ignore
            statement = (
                select(Job)
                .join(Job.category)  # type: ignore
                .where(Category.id == job.category_id)
                .where(Job.title == job.title)
                .where(Job.date == job.date)
            )
            if session.exec(statement).first():
                results["skipped"].append(job)
            else:
                new_job = Job(
                    title=job.title, category_id=job.category_id, date=job.date
                )
                session.add(new_job)
                results["created"].append(job)

        session.commit()

        return {
            "created_count": len(results["created"]),
            "skipped_count": len(results["skipped"]),
            "results": results,
        }


@app.get("/get_jobs")
def get_jobs():
    with Session(engine) as session:
        result = []
        statement = select(Job)

        jobs = session.exec(statement).all()

        if not jobs:
            raise HTTPException(status_code=404, detail="No jobs found")

        for job in jobs:
            res = {
                "title": job.title,
                "company": job.category.company.name,  # type: ignore
                "category": job.category.name,  # type: ignore
                "date": job.date,
            }
            result.append(res)

        return result
