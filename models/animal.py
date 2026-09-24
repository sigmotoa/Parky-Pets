from pydantic import BaseModel

from enums.alivestatus import AliveStatus
from enums.breed import Breed
from enums.gender import Gender


class AnimalBase(BaseModel):
    id:str #TODO UUID
    name:str
    species:str = "Dog" #TODO Add more animals
    breed:Breed
    birth_day:str #TODO update to a good data type
    gender:Gender
    status:AliveStatus = AliveStatus.ALIVE

