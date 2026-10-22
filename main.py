from fastapi import FastAPI

from data.db.animal import create_db_tables
from routers import user, animal

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_tables()

app.include_router(router=user.router, prefix="/users", tags=["users"])
app.include_router(router=animal.router, prefix="/animals", tags=["animals"])