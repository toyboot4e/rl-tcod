from enum import Enum

class EDir(Enum):
    """
    Eight directions that follow numpads. G or 5 means None direction.
    """

    NW = 9
    N = 8
    NE = 7
    E = 6
    G = 5 # G: Ground
    W = 4
    SE = 3
    S = 2
    SW = 1

    def x(self):
        return (self.value - 1) % 3

    def y(self):
        return (self.value - 4) / 3 * -1
