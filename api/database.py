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
            "amazon_general": Category(
                company_id=companies["amazon"].id,
                name="General",
                url="https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=recent&country%5B%5D=USA",
            ),
            "microsoft_general": Category(
                company_id=companies["microsoft"].id,
                name="General",
                url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true&ulcs=true&cc=United%20States&ref=cms",
            ),
            "apple_general": Category(
                company_id=companies["apple"].id,
                name="General",
                url="https://jobs.apple.com/en-us/search?location=united-states-USA",
            ),
        }
        session.add_all(categories.values())
        session.commit()


def reset_database(engine):
    print("Resetting the database...")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
