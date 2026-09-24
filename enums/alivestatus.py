from enum import Enum, auto


class AliveStatus(Enum):
    ALIVE = auto()
    DEAD = auto()
    SICK  = auto()