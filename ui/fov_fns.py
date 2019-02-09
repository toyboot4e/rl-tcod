import tcod
from engine import Stage, Tile


def init_fov(stage: Stage) -> tcod.map.Map:
    fov_map = tcod.map_new(stage.size.w, stage.size.h)

    for (x, y) in stage.size.to_range():
        tcod.map_set_properties(fov_map, x, y, not stage.tile_at(x, y).is_block_sight,
                                not stage.tile_at(x, y).is_block)

    return fov_map


def refresh_fov(fov_map: tcod.map.Map, x: int, y: int, r: int, will_light_walls: bool = True, algorithm: int = 0) -> None:
    tcod.map_compute_fov(fov_map, x, y, r, will_light_walls, algorithm)
