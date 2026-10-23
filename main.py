from fastapi import FastAPI

from data.db.db_connection import create_db_tables
from routers import user,product

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_tables()

app.include_router(router=user.router, prefix="/users", tags=["users"])
app.include_router(router=product.router, prefix="/products", tags=["products"])