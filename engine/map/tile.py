

class Tile(object):
    def __init__(self, is_block, is_block_diagonally, is_block_sight):
        self.is_block: bool = is_block
        self.is_block_diagonally: bool = is_block_diagonally
        self.is_block_sight: bool = is_block_sight

