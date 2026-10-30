from enum import Enum, auto


class IdType(str,Enum):
    CEDULA = "Cedula"
    PASAPORTE = "Pasaporte"
    NIT = "NIT"
    Extranjeria = "Extranjeria"