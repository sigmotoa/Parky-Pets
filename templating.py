from pathlib import Path
from fastapi.templating import Jinja2Templates

#TODO: Fix the imports for the enums
from enums.id_type import IdType
from enums.breed import Breed
from enums.product_category import ProductCategory

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

templates.env.globals["app_name"] = "Parky-Pets"
templates.env.globals["idType"] = IdType

templates.env.globals["app_name"]= "Parky Pets"
#templates.env.globals["product_category"] = ProductCategory
templates.env.globals.update({
    "ProductCategory": ProductCategory,
    "Breeds": Breed
})