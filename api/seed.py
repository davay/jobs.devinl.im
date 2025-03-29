import asyncio

from database import get_engine, reset_database, seed_database


async def main():
    engine = get_engine()
    reset_database(engine)
    seed_database(engine)


if __name__ == "__main__":
    asyncio.run(main())
