from typing import TYPE_CHECKING
from engine import Entity

class Actor(object):
    """
    A component to let the entity take turn.
    """

    def __init__(self, entity: Entity):
        self.entity: Entity = entity

