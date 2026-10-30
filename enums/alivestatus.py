from enum import Enum, auto


class AliveStatus(str,Enum):
    ALIVE = "Alive"
    DEAD = "Dead"
    SICK  = "Sick"