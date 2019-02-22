from typing import Iterable
from engine import Entity, Action


class Actor(object):
    """
    A component to let the entity take turn.
    """

    def __init__(self, entity: Entity):
        self.entity: Entity = entity

    def take_turn(self) -> Iterable[Action]:
        pass
