from engine.prims import Pos
from engine import Entity

class Body(object):
    def __init__(self, entity: 'Entity', pos: Pos):
        self.entity = 'Entity'
        self.pos: Pos = pos
    # def can_walk_in(self, dir: EDir) -> bool:
        # uu
