from fastapi import APIRouter, status, HTTPException, UploadFile, Form, File, Request
from starlette.responses import RedirectResponse

from data.db.operations.animal_operations_db import create_animal_db, show_all_animals_db, show_one_animal_db, update_animal_db, \
    delete_animal_db
from data.image_storage import save_image
from enums.alivestatus import AliveStatus
from enums.breed import Breed
from enums.gender import Gender
from models.animal import AnimalBase, AnimalStatusUpdate, AnimalID
from templating import templates

animals_list:list[AnimalBase] = []

router = APIRouter()

@router.get("/new_animal")
def new_animal_form(request: Request):
    return templates.TemplateResponse(request, "animals/new_animal.html", {"title": "New Animal", "breeds": [e.value for e in Breed], "genders": [e.value for e in Gender], "status": [e.value for e in AliveStatus]})


@router.post("/", status_code=status.HTTP_201_CREATED, response_class=RedirectResponse)
def create_animal(request:Request,
                  name: str = Form(...),
                  species: str = Form(...),
                  breed: Breed = Form(...),
                  birth_day: str = Form(...),
                  gender: Gender = Form(...),
                  status: AliveStatus = Form(...),
                  image:UploadFile = File(...)):

    image_url = save_image(image, "animals")
    new_animal = AnimalBase(name=name,
                            species=species,
                            breed=breed,
                            birth_day=birth_day,
                            gender=gender,
                            status=status,
                            image_url=image_url)

    #status = animal.create_animal(new_animal)
    ##animals_list.append(new_animal)
    #if status:
     #   return status
    #else:
     #   raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Animal not found")
    try:
        create_animal_db(new_animal)
        return RedirectResponse("/animales")
    except Exception as e:
        raise e


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
    one_animal = show_one_animal_db(id)
    if not one_animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        return one_animal

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=AnimalBase)
def update_animal_status(id: str, new_status: AnimalStatusUpdate):
    '''if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        for animal in animals_list:
            if animal.id == id:
                animal.status = new_status.alive
                return animal
        return None
'''
    return update_animal_db(id, new_status)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animal(id: str):

    delete_animal_db(id)
    return show_one_animal_db(id)


@router.post("/image",status_code=status.HTTP_201_CREATED)
def upload_image(file:UploadFile):
    return save_image(file, "animals")





