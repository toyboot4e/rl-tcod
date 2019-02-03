

class Pos(object):
    """
    A 2D integer vector that represents a grid position.
    """

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def add_xy(self, x: int, y: int):
        self.x += x
        self.y += y

class Size(object):
    """
    A 2D integer vector that represents a size.
    """

    def __init__(self, w: int, h: int):
        self.w, self.h = w, h

    def area(self) -> int:
        return self.w * self.h

class Rect(object):
    """
    A 2D rectangle.
    """

    def __init__(self, x, y, w, h):
        self.pos: Pos = Pos(w, h)
        self.size: Size = Size(w, h)

    @staticmethod
    def from_vec(pos: Pos, size: Size) -> 'Self':
        return Rect(pos.x, pos.y, size.w, size.h)
