import tcod
from typing import Tuple
import engine
from engine import contents, comps, input_handler
from engine import Entity, EntityFactory, GameMap, Tile
from engine.dungen import DunGen
from ui import render_all, clear_all


def main():
    WIN_TITLE: str = 'RL Tutorial'
    SCR_W, SCR_H = 64, 36
    MAP_W, MAP_H = 80, 45

    tcod.console_set_custom_font(
        contents.Fonts.ARIAL_10_10, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_W, SCR_H, title=WIN_TITLE, fullscreen=False)

    con = tcod.console_new(SCR_W, SCR_H)
    map = GameMap(MAP_W, MAP_H)
    DunGen(map).create(9, 2, 8)

    player = EntityFactory().actor().art(
        '@', [255, 255, 255]).pos(20, 20).build()
    npc = EntityFactory().actor().art('N', [255, 255, 255]).pos(10, 10).build()

    entities = [player, npc]

    key, mouse = tcod.Key(), tcod.Mouse()
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, map,  entities, SCR_W, SCR_H)
        tcod.console_flush()
        clear_all(con, entities)

        cmd = input_handler.handle_keys(key)

        move = cmd.get('move')
        exit = cmd.get('exit')
        fullscreen = cmd.get('fullscreen')

        if move is not None:
            dx, dy = move
            player.body.pos.add(dx, dy)

        if exit is not None:
            return True

        if fullscreen is not None:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
