from typing import List
from random import randint
from .dungeon import Dungeon
from engine.prims import Size, Pos, Rect
from engine.map import GameMap, Tile
from engine import Entity


class DunGen:

    def __init__(self, game_map: GameMap):
        self.game_map = game_map
        self.rooms: List[Rect] = []

    def place_rand(self, *entities: Entity) -> 'DunGen':
        for e in entities:
            room = self.rooms[randint(0, len(self.rooms) - 1)]
            e.body.set_pos(Pos(randint(room.left(), room.right()),
                               randint(room.top(), room.bottom())))
        return self

    def create(self, n_max_rooms: int, room_min_size: int, room_max_size: int) -> 'DunGen':
        map_width, map_height = self.game_map.size.to_tuple()
        for _ in range(0, n_max_rooms):
            w: int = randint(room_min_size, room_max_size)
            h: int = randint(room_min_size, room_max_size)
            x: int = randint(0, map_width - w - 1)
            y: int = randint(0, map_height - h - 1)

            new_room = Rect(x, y, w, h)
            if len(self.rooms) == 0:
                self.rooms.append(new_room)
                print(new_room)
                continue

            if any(new_room.intersects(other) for other in self.rooms):
                continue

            print(new_room)

            prev = self.rooms[-1].center()
            new = new_room.center()
            if randint(0, 1) == 1:
                self._create_h_tunnel(prev.x, new.x, prev.y)
                self._create_v_tunnel(prev.y, new.y, new.x)
            else:
                self._create_v_tunnel(prev.y, new.y, prev.x)
                self._create_h_tunnel(prev.x, new.x, new.y)

            self.rooms.append(new_room)

        for room in self.rooms:
            self._create_room(room)

        return self

    def _create_h_tunnel(self, left: int, right: int, y: int) -> None:
        for x in range(min(left, right), max(left, right) + 1):
            tile = self.game_map.tile_at(x, y)
            tile.set_params(False, is_block_sight=False, is_block_diag=False)

    def _create_v_tunnel(self, top: int, bottom: int, x: int) -> None:
        for y in range(min(top, bottom), max(top, bottom)):
            tile = self.game_map.tile_at(x, y)
            tile.set_params(False, is_block_sight=False, is_block_diag=False)

    def _create_room(self, rect: Rect) -> None:
        for (x, y) in rect.each_cells():
            tile = self.game_map.tile_at(x, y)
            tile.set_params(False, is_block_sight=False, is_block_diag=False)
