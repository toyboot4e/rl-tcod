from typing import List
from engine.prims import Size
from engine.stage import Tile, Block


class Stage(object):
    """
    The model of the game maps. Unwalkable by default.
    """

    def __init__(self, w: int, h: int) -> None:
        self.size: Size = Size(w, h)
        self.tiles: List[Tile] = [Tile(Block(True, True, True), False)
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
