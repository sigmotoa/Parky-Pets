import csv
from models.animal import AnimalBase, AnimalID
from enums import *

data_base = "animal.csv"

column_fields = [
    "id",
    "name",
    "species",
    "breed",
    "birth_day",
    "gender",
    "status"
]

def auto_id():
    try:
        with open(data_base,"r") as csvfile:
            reader = csv.DictReader(csvfile, column_fields)
            max_id = max(
                int(row["id"]) for row in reader
            )
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_animal_into_csv(register: AnimalID):
    with open(
        data_base, mode="a", newline=""
    ) as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=column_fields,
        )
        writer.writerow(register.model_dump())


def create_animal(animal: AnimalBase):
    new_id = auto_id()
    new_animal_ID = AnimalID(
        id=new_id,
        **animal.model_dump()
    )

    write_animal_into_csv(new_animal_ID)
    return new_animal_ID

def read_all_animals():
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=column_fields)
        return [AnimalBase(**row) for row in reader]

def read_one_animal_by_id(animal_id: str):
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=column_fields)
        for row in reader:
            if row["id"] == animal_id:
                return AnimalBase(**row)
        return None















