from enum import Enum
from typing import cast


class EDir(Enum):
    """
    Eight directions that follow numpads. G or 5 means None direction.
    """

    NW = 9
    N = 8
    NE = 7
    E = 6
    G = 5  # G: Ground
    W = 4
    SE = 3
    S = 2
    SW = 1

    def as_int(self) -> int:
        return cast(int, self.value)

    def x(self) -> int:
        return (self.as_int() - 1) % 3

    def y(self) -> int:
        return (self.as_int() - 4) // -3
