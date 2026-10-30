from enum import Enum, auto


class Gender(str,Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"