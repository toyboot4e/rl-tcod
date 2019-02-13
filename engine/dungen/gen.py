from typing import List
from random import randint
import tcod
from engine.prims import Size, Pos, Rect
from engine.stage import Stage, Tile
from engine import Entity, EntityFactory


class DunGen:
    """Dungeon gnenerator.
    """

    def __init__(self, stage: Stage):
        self.stage = stage
        self.rooms: List[Rect] = []

    def place_rand(self, *entities: Entity) -> 'DunGen':
        for e in entities:
            room = self.rooms[randint(0, len(self.rooms) - 1)]
            e.body.set_pos(Pos(randint(room.left(), room.right()),
                               randint(room.top(), room.bottom())))
        return self

    def create(self, n_max_rooms: int, room_min_size: int, room_max_size: int) -> 'DunGen':
        map_width, map_height = self.stage.size.to_tuple()
        for _ in range(0, n_max_rooms):
            w: int = randint(room_min_size, room_max_size)
            h: int = randint(room_min_size, room_max_size)
            x: int = randint(0, map_width - w - 1)
            y: int = randint(0, map_height - h - 1)

            new_room = Rect(x, y, w, h)
            if len(self.rooms) == 0:
                self.rooms.append(new_room)
                continue

            if any(new_room.intersects(other) for other in self.rooms):
                continue

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
            tile = self.stage.tile_at(x, y)
            tile.set_block(False, is_blocked_sight=False,
                           is_blocked_diag=False)

    def _create_v_tunnel(self, top: int, bottom: int, x: int) -> None:
        for y in range(min(top, bottom), max(top, bottom)):
            tile = self.stage.tile_at(x, y)
            tile.set_block(False, is_blocked_sight=False,
                           is_blocked_diag=False)

    def _create_room(self, rect: Rect) -> None:
        for (x, y) in rect.each():
            tile = self.stage.tile_at(x, y)
            tile.set_block(False, is_blocked_sight=False,
                           is_blocked_diag=False)

    def create_monsters(self, entities: List[Entity], max_per_room: int) -> 'DunGen':
        for r in self.rooms:
            self._create_monsters_in_room(r, entities, max_per_room)
        return self

    def _create_monsters_in_room(self, rect: Rect, entities: List[Entity], max_per_room: int) -> 'DunGen':
        # Get a random number of monsters
        number_of_monsters = randint(0, max_per_room)

        for _ in range(number_of_monsters):
            # Choose a random location in the room
            x = randint(rect.left(), rect.right())
            y = randint(rect.top(), rect.bottom())
            pos = Pos(x, y)

            monster: Entity
            if not any(e for e in entities if e.body.pos == pos):
                if randint(0, 100) < 80:
                    monster = EntityFactory().pos(x, y).art(
                        'o', tcod.desaturated_green).build()
                else:
                    monster = EntityFactory().pos(x, y).art('o', tcod.darker_green).build()

                entities.append(monster)

        return self
