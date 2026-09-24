from pydantic import BaseModel, EmailStr
from enums.id_type import IdType


class UserBase(BaseModel):
    id:str #TODO UUID
    first_name: str
    last_name: str
    id_type: IdType
    id_number: str
    phone_number: str
    email: EmailStr


class UserUpdate(BaseModel):
    first_name: str