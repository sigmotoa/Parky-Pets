from sqlmodel import SQLModel, Session, select
from .db_connection import engine
from models.product import ProductBase, ProductID


def create_one_product_db(new_product:ProductBase):
    session = Session(engine)
    product = ProductID.model_validate(new_product)
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return product

def read_all_products_db():
    session = Session(engine)
    products = session.exec(select(ProductID)).all()
    session.close()
    return products


def read_one_product_db(product_id:int):
    session = Session(engine)
    product = session.get(ProductID,product_id)
    session.close()
    return product


def update_one_product_db(product_id:int,new_price:float):
    product = read_one_product_db(product_id)
    product.price = new_price
    session = Session(engine)
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return product



