from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from data.image_storage import IMAGES_URL,IMAGES_DIR


from data.user_db import create_db_and_tables
from routers import user

app = FastAPI()
app.mount(IMAGES_URL, StaticFiles(directory=IMAGES_DIR), name="images")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router=user.router, prefix="/users", tags=["users"])