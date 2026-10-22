from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field, SQLModel

from enums.alivestatus import AliveStatus
from enums.breed import Breed
from enums.gender import Gender


class AnimalBase(SQLModel):
    ##id:str #TODO UUID
    name:str
    species:str = "Dog" #TODO Add more animals
    breed:Breed
    birth_day:str #TODO update to a good data type
    gender:Gender
    status:AliveStatus = AliveStatus.ALIVE

class AnimalStatusUpdate(SQLModel):
    alive:AliveStatus


class AnimalID(AnimalBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)