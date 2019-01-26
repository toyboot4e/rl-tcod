

class Pos(object):
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
    def add_xy(self, x: int, y: int):
        self.x += x
        self.y += y

class Size(object):
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
    def area(self) -> int:
        return self.w * self.h

class Rect(object):
    def __init__(self, x, y, w, h):
        self.pos: Pos = Pos(w, h)
        self.size: Size = Size(w, h)

