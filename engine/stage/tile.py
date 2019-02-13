from dataclasses import dataclass
from . import Block


@dataclass
class Tile(object):
    """A tile in a GameMap."""
    block: Block
    is_explored: bool

    def set_block(self, is_blocked: bool, is_blocked_diag: bool, is_blocked_sight: bool) -> None:
        self.block = Block(is_blocked, diag=is_blocked_diag,
                           sight=is_blocked_sight)

    def set_is_explored(self, is_explored: bool) -> None:
        self.is_explored = is_explored

    @property
    def is_blocked(self) -> bool:
        return self.block.tile

    @property
    def is_blocked_sight(self) -> bool:
        return self.block.sight

    @property
    def is_blocked_diag(self) -> bool:
        return self.block.diag
