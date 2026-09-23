from pydantic import BaseModel

class UserBase(BaseModel):
    id:str
    first_name: str
    last_name: str
    id_number: str #TODO let in an Enum
    phone_number: str
    email: str #TODO change to EmailStr from pydantic


class UserUpdate(BaseModel):
    first_name: str