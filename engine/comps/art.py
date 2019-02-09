from typing import List, Set, Dict, Tuple, Optional
from engine import Entity


class Art(object):
    """Holder of data for ascii visualization.
    """

    def __init__(self, entity: Entity, char: str, color: List[int]) -> None:
        self.entity: Entity = entity
        self.char: str = char
        self.color: List[int] = color
