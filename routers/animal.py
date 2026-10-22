from fastapi import APIRouter, status, HTTPException

from data.db.operations_db import create_animal_db, show_all_animals_db
from models.animal import AnimalBase, AnimalStatusUpdate, AnimalID
from data import animal

animals_list:list[AnimalBase] = []

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AnimalID)
def create_animal(new_animal:AnimalBase):
    #status = animal.create_animal(new_animal)
    ##animals_list.append(new_animal)
    #if status:
     #   return status
    #else:
     #   raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Animal not found")
    return create_animal_db(new_animal)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AnimalID])
def show_all_animals():
    '''
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animals found")
    else:
        return animals_list
        '''
    ##animals = animal.read_all_animals()
    ##return animals
    return show_all_animals_db()

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AnimalBase)
def show_one_animal(id: str):
    '''
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        for animal in animals_list:
            if animal.id == id:
                return animal
        return None
    '''
    one_animal = animal.read_one_animal_by_id(id)
    if not one_animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        return one_animal

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=AnimalBase)
def update_animal_status(id: str, new_status: AnimalStatusUpdate):
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        for animal in animals_list:
            if animal.id == id:
                animal.status = new_status.alive
                return animal
        return None









