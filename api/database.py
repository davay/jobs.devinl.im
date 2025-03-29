from sqlmodel import Session, SQLModel, create_engine, inspect

from models import Category, Company, Job

DATABASE_URL = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)


def get_engine():
    inspector = inspect(engine)
    models = [Category, Company, Job]
    tables = [model.__tablename__ for model in models]
    missing_tables = [table for table in tables if not inspector.has_table(table)]

    if missing_tables:
        print(f"Creating missing tables: {missing_tables}")
        SQLModel.metadata.create_all(engine)

    return engine


def seed_database(engine):
    print("Seeding the database...")
    with Session(engine) as session:
        companies = {
            "amazon": Company(name="Amazon"),
            "microsoft": Company(name="Microsoft"),
            "apple": Company(name="Apple"),
        }
        session.add_all(companies.values())
        session.commit()

        categories = {
            "amazon_software": Category(
                company_id=companies["amazon"].id,
                name="Software",
                url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=software-development&country%5B%5D=USA",
            ),
            "amazon_tpm": Category(
                company_id=companies["amazon"].id,
                name="Technical PM",
                url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=project-program-product-management-technical&country%5B%5D=USA",
            ),
            "amazon_ml": Category(
                company_id=companies["amazon"].id,
                name="Machine Learning",
                url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=machine-learning-science&country%5B%5D=USA",
            ),
            "amazon_ds": Category(
                company_id=companies["amazon"].id,
                name="Data Science",
                url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=data-science&country%5B%5D=USA",
            ),
            "microsoft_software": Category(
                company_id=companies["microsoft"].id,
                name="Software",
                url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&p=Software%20Engineering&l=en_us&pg=1&pgSz=20&o=Recent&flt=true",
            ),
            "microsoft_ds": Category(
                company_id=companies["microsoft"].id,
                name="Data Science",
                url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&p=Research%2C%20Applied%2C%20%26%20Data%20Sciences&l=en_us&pg=1&pgSz=20&o=Recent&flt=true",
            ),
            "microsoft_pm": Category(
                company_id=companies["microsoft"].id,
                name="Data Science",
                url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&p=Research%2C%20Applied%2C%20%26%20Data%20Sciences&l=en_us&pg=1&pgSz=20&o=Recent&flt=true",
            ),
            "apple_ml": Category(
                company_id=companies["apple"].id,
                name="Machine Learning",
                url="https://jobs.apple.com/en-us/search?location=united-states-USA&team=machine-learning-infrastructure-MLAI-MLI+deep-learning-and-reinforcement-learning-MLAI-DLRL+natural-language-processing-and-speech-technologies-MLAI-NLP+computer-vision-MLAI-CV+applied-research-MLAI-AR",
            ),
            "apple_software": Category(
                company_id=companies["apple"].id,
                name="Software",
                url="https://jobs.apple.com/en-us/search?location=united-states-USA&team=apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT",
            ),
        }
        session.add_all(categories.values())
        session.commit()


def reset_database(engine):
    print("Resetting the database...")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
