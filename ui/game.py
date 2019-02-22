import tcod
from ui import contents
from ui.scenes import RoguelikeScene


class Game(object):
    """ Provides game loop. """

    def __init__(self) -> None:
        WIN_TITLE: str = 'RL Tutorial'
        SCR_W, SCR_H = 64, 36
        self.scene = RoguelikeScene(SCR_W, SCR_H)
        tcod.console_set_custom_font(
            contents.Fonts.ARIAL_10_10, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
        tcod.console_init_root(SCR_W, SCR_H, title=WIN_TITLE, fullscreen=False)

    def run(self) -> None:
        key, mouse = tcod.Key(), tcod.Mouse()
        while not tcod.console_is_window_closed():
            tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)
            self.render()

    def render(self) -> None:
        self.scene.render()
