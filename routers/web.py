from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()

@router.get("/")
def index(request: Request):
    pass