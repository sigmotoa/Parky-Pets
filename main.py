from fastapi import FastAPI
from routers import user, animal

app = FastAPI()

app.include_router(router=user.router, prefix="/users", tags=["users"])
app.include_router(router=animal.router, prefix="/animals", tags=["animals"])