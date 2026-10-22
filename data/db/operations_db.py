from models.animal import AnimalID,AnimalBase
from sqlmodel import SQLModel, Session, select
from .animal import engine


def create_animal_db(new_animal:AnimalBase):
    session= Session(engine)
    animal_db = AnimalID.model_validate(new_animal)
    session.add(animal_db)
    session.commit()
    session.refresh(animal_db)
    session.close()

    return animal_db

def show_all_animals_db():
    session= Session(engine)

    animals = session.exec(select(AnimalID)).all()
    session.close()
    return animals