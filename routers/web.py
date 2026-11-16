from fastapi import APIRouter, Request

from data.db.operations.animal_operations_db import show_all_animals_db
from templating import templates

router = APIRouter()

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"title": "Inicio"})

@router.get("/animales")
def animales(request: Request):
    animales = show_all_animals_db()
    return (
        templates.TemplateResponse(
            request, "animales.html",
            {"title": "animales registrados",
             "animales": animales}))