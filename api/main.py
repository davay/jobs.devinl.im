from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import get_engine, reset_database, seed_database

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


@app.get("/")
def read_root():
    return {"Hello": "World"}
