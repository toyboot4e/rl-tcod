from typing import TYPE_CHECKING
from engine import Entity

class Actor(object):
    def __init__(self, entity: Entity):
        self.entity: Entity = entity

