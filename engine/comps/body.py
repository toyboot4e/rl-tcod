from engine.prims import Pos
from engine import Entity


class Body(object):
    """
    A component to for those who is on the GameMap.
    """

    def __init__(self, entity: 'Entity', pos: Pos):
        self.entity = 'Entity'
        self.pos: Pos = pos

    def set_pos(self, pos: Pos) -> None:
        self.pos = pos
