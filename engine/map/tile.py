

class Tile(object):
    """
    A tile in a GameMap.
    """

    def __init__(self, is_block, is_block_diag, is_block_sight):
        self.is_block: bool = is_block
        self.is_block_diag: bool = is_block_diag
        self.is_block_sight: bool = is_block_sight

