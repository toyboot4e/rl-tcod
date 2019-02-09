from engine.prims import Pos

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.comps import Actor, Body, Art


class Entity(object):
    """The generic entity of anything on the GameMap.
    """

    # TODO: use Python3 and remove those quotes
    def __init__(self) -> None:
        self.art: 'Art' = None
        self.body: 'Body' = None
        self.actor: 'Actor' = None
