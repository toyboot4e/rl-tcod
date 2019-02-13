from dataclasses import dataclass


@dataclass
class Block(object):
    tile: bool
    sight: bool
    diag: bool
