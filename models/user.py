from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import BaseModel, EmailStr
from enums.id_type import IdType


class UserBase(SQLModel):
    first_name: str
    last_name: str
    id_type: IdType
    id_number: str
    phone_number: str
    email: EmailStr


class UserUpdate(UserBase):
    first_name: str
    last_name: str | None = None
    phone_number: str | None = None
    id_type: IdType | None = None
    id_number: str| None = None
    phone_number: str| None = None
    email: str| None = None

class UserID(UserBase, table =True):
    id: Optional[int] = Field(default=None, primary_key=True)
    image_url:str| None = None
