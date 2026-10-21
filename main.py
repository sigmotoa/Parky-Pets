from fastapi import FastAPI

from data.user_db import create_db_and_tables
from routers import user

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router=user.router, prefix="/users", tags=["users"])