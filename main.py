import tcod
import engine
from engine import contents
from engine import comps
from engine import handler


def main():
    WIN_TITLE: str = 'RL Tutorial'
    SCR_W, SCR_H = 64, 36
    tcod.console_set_custom_font(contents.Fonts.ARIAL_10_10, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_W, SCR_H, title=WIN_TITLE, fullscreen=False)

    con = tcod.console_new(SCR_W, SCR_H)
    player: comps.Actor = comps.Actor()

    key, mouse =  tcod.Key(), tcod.Mouse()
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(con, tcod.white)
        tcod.console_put_char(con, player.pos.x, player.pos.y, '@', tcod.BKGND_NONE)
        tcod.console_blit(con, 0, 0, SCR_W, SCR_H, 0, 0, 0)
        tcod.console_flush()
        tcod.console_put_char(con, player.pos.x, player.pos.y, ' ', tcod.BKGND_NONE)
        
        cmd = engine.handler.handle_keys(key)

        move = cmd.get('move')
        exit = cmd.get('exit')
        fullscreen = cmd.get('fullscreen')

        if move is not None:
            dx, dy = move
            player.pos.add(dx, dy)

        if exit is not None:
            return True

        if fullscreen is not None:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()

