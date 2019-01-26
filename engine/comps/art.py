from typing import List, Set, Dict, Tuple, Optional
from engine import Entity

class Art(object):
    def __init__(self, entity: 'Entity', char: chr, color: [int, int, int]):
        self.entity: Entity = 'Entity'
        self.char: chr = char
        self.color: [int, int, int] = color
