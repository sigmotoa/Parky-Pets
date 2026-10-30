import csv
from models.product import ProductBase, ProductID

database = "products.csv"

column_fields = ["id", "name", "price", "category", "expiration_date"]

def new_id():
    try:
        with open(database, "r") as csvfile:
            reader = csv.DictReader(csvfile,column_fields)
            max_id = max(int(row["id"]) for row in reader)
            return max_id+1
    except (FileNotFoundError, ValueError):
        return 1


def write_register_csv(register:ProductID):
    with open(database, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile,column_fields,)
        writer.writerow(register.model_dump())
        csvfile.close()

def create_product_csv(new_product:ProductBase):
    id = new_id()
    new_product_id = ProductID(
        id=id,
        **new_product.model_dump()
    )
    write_register_csv(new_product_id)
    return True


def read_all_products_csv():
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)
        return [ProductID(**row) for row in reader]



def read_one_product_csv(id_product:int):
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)
        for row in reader:
            if int(row["id"]) == id_product:
                return ProductBase(**row)
        return None

