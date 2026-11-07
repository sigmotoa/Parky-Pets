from fastapi import APIRouter, Request
from data.db.operations import user_operation_db
from templating import templates

router = APIRouter(include_in_schema=True)

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html",
    {"title": "Home for ParkyPets site"})

@router.get("/usuarios")
def usuarios_page(request: Request):
    usuarios = user_operation_db.read_all_users_db()
    return templates.TemplateResponse(request, "usuarios.html",{"usuarios": usuarios, "title":"Usuarios de Parky Pets"})