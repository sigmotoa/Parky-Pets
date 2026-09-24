from enum import Enum


class Breed(str,Enum):
    UNIQUE = "Unique"
    GERMAN_SHEPHERD = "German Shepherd"
    POODLE = "Poodle"
    LABRADOR_RETRIEVER = "Labrador Retriever"
    GOLDEN_RETRIEVER = "Golden Retriever"
    FRENCH_BULLDOG = "French Bulldog"