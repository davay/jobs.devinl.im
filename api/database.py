from sqlmodel import Session, SQLModel, create_engine, inspect

from models import Category, Company, Job
from sources import all_sources

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
        for company_source in all_sources:
            company = Company(name=company_source.name)
            session.add(company)
            session.commit()

            for category_source in company_source.categories:
                category = Category(name=category_source.name, url=category_source.url)
                session.add(category)
                session.commit()


def reset_database(engine):
    print("Resetting the database...")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
