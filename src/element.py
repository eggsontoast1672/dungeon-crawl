from enum import Enum


class Element(Enum):
    FIRE = 0
    ICE = 1
    EARTH = 2

    def __str__(self) -> str:
        fmt: str
        if self.value == self.FIRE:
            fmt = "fire"
        elif self.value == self.ICE:
            fmt = "ice"
        else:
            fmt = "earth"
        return fmt
