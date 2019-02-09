from typing import List, Set, Dict, Tuple, Optional
import tcod
from tcod.console import Console
from engine import Entity, GameMap, Tile
from enum import Enum


class TilePallet:
    """
    It holds ascii pallets of tiles.
    """

    DARK_WALL = tcod.Color(0, 0, 100)
    DARK_GROUND = tcod.Color(50, 50, 150)


def render_all(con: Console, map: GameMap, entities: List[Entity], scr_w: int, scr_h: int) -> None:
    for y in range(0, map.size.h):
        for x in range(0, map.size.w):
            tile: Tile = map.tile_at(x, y)
            if tile.is_block_sight:
                # print('block at {}, {}'.format(x, y))
                tcod.console_set_char_background(
                    con, x, y, TilePallet.DARK_WALL, tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(
                    con, x, y, TilePallet.DARK_GROUND, tcod.BKGND_SET)

    for entity in entities:
        draw_entity(con, entity)

    tcod.console_blit(con, 0, 0, scr_w, scr_h, 0, 0, 0)


def draw_entity(con: Console, entity: Entity) -> None:
    tcod.console_set_default_foreground(con, entity.art.color)
    tcod.console_put_char(con, entity.body.pos.x,
                          entity.body.pos.y, entity.art.char, tcod.BKGND_NONE)


def clear_all(con: Console, entities: List[Entity]) -> None:
    for entity in entities:
        clear_entity(con, entity)


def clear_entity(con: Console, entity: Entity) -> None:
    # erase the character that represents this object
    tcod.console_put_char(con, entity.body.pos.x,
                          entity.body.pos.y, ' ', tcod.BKGND_NONE)
