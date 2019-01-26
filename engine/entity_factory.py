from engine.prims import Pos
from engine import Entity
from engine.comps import Body, Actor, Art


class EntityFactory(object):
    def __init__(self):
        self.entity = Entity()
        self.entity.body = Body(self.entity, Pos(0, 0))

    def build(self) -> Entity:
        return self.entity

    def actor(self) -> 'Self':
        self.entity.actor = Actor(self.entity)
        return self

    def art(self, char: chr, color: [int, int, int]) -> 'Self':
        self.entity.art = Art(self.entity, char, color)
        return self

    def pos(self, x: int, y: int) -> 'Self':
        self.entity.body.pos = Pos(x, y)
        return self
