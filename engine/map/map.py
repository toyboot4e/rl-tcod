from engine.prims import Size
from .tile import Tile
from typing import List


class GameMap(object):
    """
    The model of the game maps. Unwalkable by default.
    """

    def __init__(self, w, h):
        self.size: Size = Size(w, h)
        self.tiles: List[Tile] = self.initialize_tiles()

    def index(self, x, y):
        return x + y * self.size.w

    def tile_at(self, x: int, y: int):
        return self.tiles[self.index(x, y)]

    def initialize_tiles(self):
        tiles = [Tile(True, True, True) for _ in range (0, self.size.area())]

        return tiles

    # def print_all(self):
        # TODO: use
        # for y in range(0, self.size.y):
            # for x in range(0, self.size.x):
                # print
