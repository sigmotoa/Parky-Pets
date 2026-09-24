from fastapi import APIRouter, status, HTTPException

from models.animal import AnimalBase

animals_list:list[AnimalBase] = []

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_animal(new_animal:AnimalBase):
    animals_list.append(new_animal)
    return new_animal

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AnimalBase])
def show_all_animals():
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animals found")
    else:
        return animals_list









