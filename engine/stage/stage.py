from engine.prims import Size
from .tile import Tile
from typing import List


class Stage(object):
    """
    The model of the game maps. Unwalkable by default.
    """

    def __init__(self, w: int, h: int) -> None:
        self.size: Size = Size(w, h)
        self.tiles: List[Tile] = [Tile(True, True, True)
                                  for _ in range(0, self.size.area())]

    def index(self, x: int, y: int) -> int:
        return x + y * self.size.w

    def tile_at(self, x: int, y: int) -> Tile:
        return self.tiles[self.index(x, y)]

    # def print_all(self):
        # TODO: use
        # for y in range(0, self.size.y):
        # for x in range(0, self.size.x):
        # print
