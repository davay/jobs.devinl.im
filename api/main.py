import math
import os
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlmodel import Session, col, desc, or_, select

from database import get_engine
from models import (
    Category,
    Job,
    JobSearchParamsDTO,
    JobSearchResponseDTO,
    JobSearchResultDTO,
    ScrapedJobDTO,
    SourceDTO,
)

is_production = os.getenv("ENVIRONMENT") == "production"

# so that docs work https://fastapi.tiangolo.com/advanced/behind-a-proxy/
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
def submit_jobs(jobs: list[ScrapedJobDTO]):
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
                    title=job.title,
                    category_id=job.category_id,
                    date=job.date,
                    retrieval_date=job.retrieval_date,
                )
                session.add(new_job)
                results["created"].append(job)

        session.commit()

        return {
            "created_count": len(results["created"]),
            "skipped_count": len(results["skipped"]),
            "results": results,
        }


@app.post("/search_jobs", response_model=JobSearchResponseDTO)
def search_jobs(search_params: JobSearchParamsDTO):
    with Session(engine) as session:
        results = []
        statement = select(Job).order_by(desc(Job.date))

        if search_params.keywords:
            keyword_conditions = [
                col(Job.title).ilike(f"%{keyword.strip()}%")
                for keyword in search_params.keywords
            ]
            statement = statement.where(or_(*keyword_conditions))

        count_query = select(func.count()).select_from(statement.subquery())
        total_count = session.scalar(count_query)

        total_pages = 1
        if total_count:
            total_pages = math.ceil(total_count / search_params.limit)

        statement = statement.offset(search_params.page * search_params.limit).limit(
            search_params.limit
        )

        jobs = session.exec(statement).all()

        if not jobs:
            raise HTTPException(status_code=404, detail="No jobs found")

        for job in jobs:
            jobSearchResult = JobSearchResultDTO(
                title=job.title,
                company=job.category.company.name,  # type: ignore
                category=job.category.name,  # type: ignore
                url=job.category.url,  # type: ignore
                date=job.date,
                retrieval_date=job.retrieval_date,
            )
            results.append(jobSearchResult)

        jobSearchResponse = JobSearchResponseDTO(
            results=results, total_pages=total_pages
        )

        return jobSearchResponse
