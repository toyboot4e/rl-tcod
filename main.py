import tcod
import engine
from engine import contents, comps, input_handler
from engine import Entity, EntityFactory, GameMap, Tile
from ui import render_all, clear_all
from typing import Tuple


def main():
    WIN_TITLE: str = 'RL Tutorial'
    SCR_W, SCR_H = 64, 36
    MAP_W, MAP_H = 80, 45
    tcod.console_set_custom_font(contents.Fonts.ARIAL_10_10, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_W, SCR_H, title=WIN_TITLE, fullscreen=False)

    con = tcod.console_new(SCR_W, SCR_H)
    map = GameMap(MAP_W, MAP_H)

    print('visibilities:')
    for y in range(0, map.size.h):
        for x in range(0, map.size.w):
            tile: Tile = map.tile_at(x, y)
            mark = 0 if tile.is_block_sight else 1
            print(mark, end='')
        print()

    player = EntityFactory().actor().art('@', [255,255,255]).pos(20, 20).build()
    npc = EntityFactory().actor().art('N', [255,255,255]).pos(10, 10).build()
    print(player)
    print(npc)
    entities = [player, npc]

    key, mouse =  tcod.Key(), tcod.Mouse()
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

