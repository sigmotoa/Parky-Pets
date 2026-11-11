from fastapi import APIRouter, HTTPException, UploadFile, Form, File, Request
from starlette import status
from starlette.responses import RedirectResponse

from data.db.operations.product_operation_db import create_one_product_db, read_all_products_db, read_one_product_db, \
    update_one_product_db, delete_one_product_db
from data.image_storage import save_image
from enums import product_category
from enums.product_category import ProductCategory
from models.product import ProductBase, ProductID
from templating import templates

router = APIRouter()

@router.get("/new")
def new_product(request:Request):
    return templates.TemplateResponse(request, "new_product.html", {"title":"Nuevo Producto", "product_category":product_category})


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductID)
def create_product(
        name:str = Form(...),
        price:float = Form(...),
        category:ProductCategory = Form(...),
        expiration_date:str = Form(...),
        image: UploadFile = File()
):
    img_url = save_image(image,"products")
    new_product = ProductBase(
        name=name,
        price=price,
        category=category,
        expiration_date=expiration_date,
        image_url=img_url
    )
    try:
        create_one_product_db(new_product)
        return RedirectResponse("/products/", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/", response_model=list[ProductID])
def show_all_products(request:Request):
    all_products =  read_all_products_db()
    return templates.TemplateResponse(
        request, "products.html", {"title":"Productos","products":all_products}
    )


#TODO
@router.get("/{product_id}", response_model=ProductBase)
def show_one_product(product_id:int):
    one_product = read_one_product_db(product_id)
    if one_product:
        return read_one_product_db(product_id)
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.patch("/{product_id}", response_model=ProductID)
def update_product(product_id: int, new_price:float):
    return update_one_product_db(product_id, new_price)



@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int):
    if delete_one_product_db(product_id):
        return {"Product":"Deleted"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.post("/image", status_code=status.HTTP_201_CREATED)
def add_img(image:UploadFile):
    return save_image(image,"products")