from sqlmodel import Session, SQLModel, create_engine, inspect

from models import Category, Company, Job
from sources import all_sources

DATABASE_URL = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
models = [Category, Company, Job]


def get_engine():
    inspector = inspect(engine)
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

            categories = []
            for category_source in company_source.categories:
                category = Category(
                    name=category_source.name,
                    url=category_source.url,
                    company_id=company.id,
                )
                categories.append(category)

            session.add_all(categories)
            session.commit()


def reset_database(engine):
    print("Resetting the database...")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
