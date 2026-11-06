from fastapi import FastAPI

from routers import animal, web, product, user

from data.db.db_connection import create_db_tables

from fastapi.staticfiles import StaticFiles
from data.image_storage import IMAGES_URL,IMAGES_DIR
from templating import BASE_DIR



async def lifespan(app:FastAPI):
    create_db_tables()
    yield

app = FastAPI(lifespan=lifespan, title="Parky PETS")
app.mount(IMAGES_URL, StaticFiles(directory=IMAGES_DIR), name="images")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


##@app.on_event("startup")
#def on_startup():
#    create_db_tables()

app.include_router(router=web.router, tags=["WEB"])
app.include_router(router=user.router, prefix="/users", tags=["users"])
app.include_router(router=animal.router, prefix="/animals", tags=["animals"])
app.include_router(router=product.router, prefix="/products", tags=["products"])