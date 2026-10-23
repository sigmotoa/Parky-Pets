from pydantic import BaseModel
from enums.product_category import ProductCategory
from sqlmodel import SQLModel, Field
from typing import Optional



class ProductBase(SQLModel):
    name:str
    price:float
    category:ProductCategory
    expiration_date:str


class ProductID(ProductBase, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
