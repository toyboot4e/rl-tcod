import tcod
from typing import Tuple, List, TYPE_CHECKING
import engine
from engine import comps, input_handler
from engine import Entity, EntityFactory, Stage, Tile
from engine.prims import Pos, Size
from engine.dungen import DunGen
from ui import render_fns, fov_fns
from . import Scene


class RoguelikeScene(Scene):

    def __init__(self, scr_w: int, scr_h: int) -> None:
        self.console = tcod.console_new(scr_w, scr_h)
        self.stage = Stage(scr_w, scr_h)
        self.entities: List[Entity] = []
        self.player = Entity()
        self.entities.append(self.player)

    def construct(self) -> None:
        EntityFactory(self.player).actor().art(
            '@', [255, 255, 255]).pos(20, 20).build()

        DunGen(self.stage).create(9, 2, 7) \
                          .place_rand(self.player) \
                          .create_monsters(self.entities, 4)
        self.fov_map = fov_fns.init_fov(self.stage)

    def render(self) -> None:
        tcod.console_flush()
        # map and entities
        render_fns.clear_all(self.console, self.entities)
        # fov
        self.update_fov()
        scr_w, scr_h = tcod.sys_get_current_resolution()
        render_fns.render_all(self.console, self.stage,
                              self.fov_map, self.entities, scr_w, scr_h)

    def update_fov(self) -> None:
        fov_r = 6
        fov_fns.refresh_fov(self.fov_map, self.player.body.pos.x,
                            self.player.body.pos.y, fov_r, True, 0)

    def handle_imput(self, key: tcod.Key, mouse: tcod.Mouse) -> None:
        cmd = input_handler.handle_keys(key)

        move = cmd.get('move')
        if move is not None:
            dx, dy = move
            next = self.player.body.pos.offset(dx, dy)
            if not self.stage.tile_at(next.x, next.y).is_blocked:
                self.player.body.set_offset(Pos(dx, dy))

        exit = cmd.get('exit')
        if exit is not None:
            return

        fullscreen = cmd.get('fullscreen')
        if fullscreen is not None:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
