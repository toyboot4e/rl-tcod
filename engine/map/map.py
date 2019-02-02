from engine.prims import Size
from .tile import Tile
from typing import List


class GameMap(object):
    """
    The model of the game maps.
    """

    def __init__(self, w, h):
        self.size: Size = Size(w, h)
        self.tiles: List[Tile] = self.initialize_tiles()

    def index(self, x, y):
        return x + y * self.size.w

    def tile_at(self, x: int, y: int):
        return self.tiles[self.index(x, y)]

    def initialize_tiles(self):
        # anti pattern: tiles = [Tile(False, False, False)] * (self.size.w * self.size.h)
        # it's only for value types, not referenced types.
        tiles = [Tile(False, False, False) for _ in range (0, self.size.area())]

        y = 22
        for x in range(0,33):
            print(x,y)
            tile = tiles[self.index(x, y)]
            tile.is_block = True
            tile.is_block_sight = True

        return tiles

    # def print_all(self):
        # TODO: use
        # for y in range(0, self.size.y):
            # for x in range(0, self.size.x):
                # print
