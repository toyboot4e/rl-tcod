

class Tile(object):
    """
    A tile in a GameMap.
    """

    def __init__(self, is_block: bool, is_block_diag: bool, is_block_sight: bool) -> None:
        self.is_block: bool = is_block
        self.is_block_diag: bool = is_block_diag
        self.is_block_sight: bool = is_block_sight
        self.is_explored: bool = False

    def set_params(self, is_block: bool, is_block_diag: bool, is_block_sight: bool) -> None:
        self.is_block = is_block
        self.is_block_diag = is_block_diag
        self.is_block_sight = is_block_sight

    def set_is_explored(self, is_explored: bool) -> None:
        self.is_explored = is_explored
