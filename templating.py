from pathlib import Path
from fastapi.templating import Jinja2Templates

from enums.id_type import IdType

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

templates.env.globals["app_name"] = "Parky-Pets"
templates.env.globals["idType"] = IdType
