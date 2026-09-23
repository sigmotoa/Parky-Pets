from fastapi import FastAPI
from routers import user

app = FastAPI()

app.include_router(router=user.router, prefix="/users", tags=["users"])