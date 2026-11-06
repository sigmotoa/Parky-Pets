from fastapi import APIRouter, Request

from templating import templates

router = APIRouter(include_in_schema=True)

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")