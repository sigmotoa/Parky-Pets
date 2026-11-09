from fastapi import APIRouter, HTTPException, UploadFile, Form, File
from starlette import status

from data.db.operations.product_operation_db import create_one_product_db, read_all_products_db, read_one_product_db, \
    update_one_product_db, delete_one_product_db
from data.image_storage import save_image
from enums.product_category import ProductCategory
from models.product import ProductBase, ProductID

router = APIRouter()



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
       return create_one_product_db(new_product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




@router.get("/", response_model=list[ProductID])
def show_all_products():
    return read_all_products_db()


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