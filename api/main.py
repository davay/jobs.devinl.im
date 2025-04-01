import math
import os
from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, nullslast
from sqlmodel import Session, asc, col, desc, or_, select

from database import get_engine
from models import (
    Category,
    Company,
    Job,
    JobSearchParamsDTO,
    JobSearchResponseDTO,
    JobSearchResultDTO,
    ScrapedJobDTO,
    SourceDTO,
    SubmitJobsResponseDTO,
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

        statement = (
            select(Category)
            .where(Category.company_id == Company.id)
            .order_by(
                asc(Company.name),
                desc(Category.name),
            )
        )

        categories = session.exec(statement).all()

        if not categories:
            raise HTTPException(status_code=404, detail="No categories found")

        # comparison happens on server because i dont want to deal with timezones
        current_time = datetime.now()
        for category in categories:
            last_refreshed_string = "Never"
            if category.last_refreshed:
                last_refreshed_delta = current_time - category.last_refreshed
                total_seconds = int(last_refreshed_delta.total_seconds())
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                last_refreshed_string = f"{hours}h {minutes}m ago"

            data = {
                # ignored err, company is guaranteed to exist by design, sqlmodel quirk forces optional type in definition
                "company_name": category.company.name,  # type: ignore
                "category_id": category.id,
                "category_name": category.name,
                "url": category.url,
                "last_refreshed": last_refreshed_string,
            }
            result.append(data)

        return result


@app.post("/submit_jobs", response_model=SubmitJobsResponseDTO)
def submit_jobs(jobs: list[ScrapedJobDTO]):
    with Session(engine) as session:
        submit_jobs_response = SubmitJobsResponseDTO(created_count=0)

        # v1, this works
        # if first_batch:
        #     statement = select(Job)
        #     existing_jobs = session.exec(statement).all()
        #     session.delete(existing_jobs)
        #     session.commit()

        # v2, delete all jobs from first encounter of a category
        # should feel less awkward during refresh times
        updated_categories = set()
        for job in jobs:
            if job.category_id not in updated_categories:
                statement = select(Job).where(Job.category_id == job.category_id)
                existing_jobs = session.exec(statement).all()
                for existing_job in existing_jobs:
                    session.delete(existing_job)
                session.commit()

            cleaned_date = None
            if job.date and job.date != "None":
                try:
                    cleaned_date = datetime.fromisoformat(job.date)
                except Exception as e:
                    print(f"Error {e} while submitting job: {job}")
                    pass

            new_job = Job(
                title=job.title,
                category_id=job.category_id,
                date=cleaned_date,
            )
            session.add(new_job)
            session.commit()
            submit_jobs_response.created_count += 1
            updated_categories.add(job.category_id)

        # update each category's last_refreshed date only once
        current_time = datetime.now()
        for category_id in updated_categories:
            category = session.get(Category, category_id)
            if category:
                category.last_refreshed = current_time

        session.commit()
        return submit_jobs_response


@app.post("/search_jobs", response_model=JobSearchResponseDTO)
def search_jobs(search_params: JobSearchParamsDTO):
    with Session(engine) as session:
        results = []

        # unknown dates go behind
        statement = (
            select(Job)
            .where(Job.category_id == Category.id)
            .where(Category.company_id == Company.id)
            .order_by(
                nullslast(desc(Job.date)),
                asc(Company.name),
                desc(Category.last_refreshed),
            )
        )

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

        current_time = datetime.now()
        for job in jobs:
            last_refreshed_delta = current_time - job.category.last_refreshed  # type: ignore
            total_seconds = int(last_refreshed_delta.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            last_refreshed_string = f"{hours}h {minutes}m ago"

            jobSearchResult = JobSearchResultDTO(
                title=job.title,
                company=job.category.company.name,  # type: ignore
                category=job.category.name,  # type: ignore
                url=job.category.url,  # type: ignore
                date=job.date,
                last_refreshed=last_refreshed_string,
            )
            results.append(jobSearchResult)

        jobSearchResponse = JobSearchResponseDTO(
            results=results, total_pages=total_pages
        )

        return jobSearchResponse
