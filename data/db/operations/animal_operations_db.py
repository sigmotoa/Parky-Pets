from enums import alivestatus
from models.animal import AnimalID, AnimalBase, AnimalStatusUpdate
from sqlmodel import SQLModel, Session, select
from data.db.animal import engine


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


def show_one_animal_db(animal_id: int):
    session= Session(engine)
    animal_db = session.get(AnimalID, animal_id)
    session.close()
    return animal_db


def update_animal_db(animal_id: int, status:AnimalStatusUpdate):
    session= Session(engine)
    animal_db = session.get(AnimalID, animal_id)
    print(status)
    animal_db.status = status.status
    session.add(animal_db)
    session.commit()
    session.refresh(animal_db)

    session.close()
    return animal_db

def delete_animal_db(animal_id: int):
    #session= Session(engine)
    #session.commit()
    #session.close()
    #animal_status: AnimalStatusUpdate
    #animal_status = alivestatus.AliveStatus.DEAD
    #status: alivestatus.AliveStatus = alivestatus.AliveStatus.DEAD
    status = AnimalStatusUpdate
    status.status = alivestatus.AliveStatus.DEAD
    animal = update_animal_db(animal_id, status)
    #return True

