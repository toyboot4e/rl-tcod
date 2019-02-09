from engine.prims import Pos
from engine import Entity
from engine.comps import Body, Actor, Art
from typing import List


class EntityFactory(object):
    """ A helper for making entities.
    """

    def __init__(self) -> None:
        self.entity = Entity()
        self.entity.body = Body(self.entity, Pos(0, 0))

    def build(self) -> Entity:
        return self.entity

    def actor(self) -> 'EntityFactory':
        self.entity.actor = Actor(self.entity)
        return self

    def art(self, char: str, color: List[int]) -> 'EntityFactory':
        self.entity.art = Art(self.entity, char, color)
        return self

    def pos(self, x: int, y: int) -> 'EntityFactory':
        self.entity.body.pos = Pos(x, y)
        return self
