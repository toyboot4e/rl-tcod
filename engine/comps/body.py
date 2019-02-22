from engine.prims import Pos
from engine import Entity
from engine.stage import Block


class Body(object):
    """
    A component to for those who is on the GameMap.
    """

    def __init__(self, entity: Entity, pos: Pos, block: Block = Block(True, False, True)):
        self.entity = Entity
        self.pos: Pos = pos
        self.block = Block

    def set_pos(self, pos: Pos) -> None:
        self.pos = pos

    def set_offset(self, offset: Pos) -> None:
        self.pos = self.pos + offset

    @property
    def is_blocked(self) -> bool:
        return self.block.tile

    def is_blocked_sight(self) -> bool:
        return self.block.sight
