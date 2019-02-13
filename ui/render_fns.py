from typing import List, Set, Dict, Tuple, Optional
import tcod
from tcod.console import Console
from engine import Entity, Stage, Tile
from engine.prims import Rect
from enum import Enum


class TilePallet:
    """It holds ascii pallets of tiles.
    """

    DARK_WALL = tcod.Color(0, 0, 100)
    DARK_GROUND = tcod.Color(50, 50, 150)
    LIGHT_WALL = tcod.Color(130, 110, 50)
    LIGHT_GROUND = tcod.Color(200, 180, 50)


def render_all(con: Console, stage: Stage, fov_map: tcod.map.Map, entities: List[Entity], scr_w: int, scr_h: int) -> None:
    for (x, y) in stage.size.each():
        tile = stage.tile_at(x, y)

        color: tcod.Color
        if tcod.map_is_in_fov(fov_map, x, y):
            color = TilePallet.LIGHT_WALL if tile.is_blocked_sight else TilePallet.LIGHT_GROUND
            tile.set_is_explored(True)
        elif tile.is_explored:
            color = TilePallet.DARK_WALL if tile.is_blocked_sight else TilePallet.DARK_GROUND
        else:
            continue

        tcod.console_set_char_background(con, x, y, color, tcod.BKGND_SET)

    for entity in entities:
        draw_entity(con, entity, fov_map)

    tcod.console_blit(con, 0, 0, scr_w, scr_h, 0, 0, 0)


def draw_entity(con: Console, entity: Entity, fov_map: tcod.map.Map) -> None:
    if not tcod.map_is_in_fov(fov_map, entity.body.pos.x, entity.body.pos.y):
        return
    tcod.console_set_default_foreground(con, entity.art.color)
    tcod.console_put_char(con, entity.body.pos.x,
                          entity.body.pos.y, entity.art.char, tcod.BKGND_NONE)


def clear_all(con: Console, entities: List[Entity]) -> None:
    for entity in entities:
        clear_entity(con, entity)


def clear_entity(con: Console, entity: Entity) -> None:
    tcod.console_put_char(con, entity.body.pos.x,
                          entity.body.pos.y, ' ', tcod.BKGND_NONE)
