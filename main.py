import tcod
from typing import Tuple
import engine
from engine import contents, comps, input_handler
from engine import Entity, EntityFactory, Stage, Tile
from engine.prims import Pos
from engine.dungen import DunGen
from ui import render_fns, fov_fns


def main():
    WIN_TITLE: str = 'RL Tutorial'
    SCR_W, SCR_H = 64, 36
    MAP_W, MAP_H = 64, 36

    tcod.console_set_custom_font(
        contents.Fonts.ARIAL_10_10, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_W, SCR_H, title=WIN_TITLE, fullscreen=False)

    con = tcod.console_new(SCR_W, SCR_H)
    stage = Stage(MAP_W, MAP_H)

    player: Entity = EntityFactory().actor().art(
        '@', [255, 255, 255]).pos(20, 20).build()
    npc: Entity = EntityFactory().actor().art(
        'N', [255, 255, 255]).pos(10, 10).build()

    entities = [player, npc]

    DunGen(stage).create(9, 2, 7).place_rand(player, npc)
    fov_map = fov_fns.init_fov(stage)
    fov_r = 6
    fov_fns.refresh_fov(fov_map, player.body.pos.x,
                        player.body.pos.y, fov_r, True, 0)

    key, mouse = tcod.Key(), tcod.Mouse()
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        fov_fns.refresh_fov(fov_map, player.body.pos.x,
                            player.body.pos.y, fov_r, True, 0)

        render_fns.render_all(con, stage, fov_map, entities, SCR_W, SCR_H)
        tcod.console_flush()
        render_fns.clear_all(con, entities)

        cmd = input_handler.handle_keys(key)

        move = cmd.get('move')
        if move is not None:
            dx, dy = move
            next = player.body.pos.add(dx, dy)
            if not stage.tile_at(next.x, next.y).is_block:
                player.body.set_pos(player.body.pos.add(dx, dy))

        exit = cmd.get('exit')
        if exit is not None:
            return True

        fullscreen = cmd.get('fullscreen')
        if fullscreen is not None:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
