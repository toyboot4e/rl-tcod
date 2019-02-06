

class Pos(object):
    """
    A 2D integer vector that represents a grid position.
    """

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def add(self, x: int, y: int) -> 'Self':
        return Pos(self.x + x, self.y + y)

    def __str__(self):
        return format('Pos({0}, {1})', self.w, self.h)

    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
        elif isinstance(other, Size):
            return Pos(self.x + other.w, self.y + other.h)
        else:
            return NotImplemented

    def __sub__(self, other) -> 'Self':
        if isinstance(other, Pos):
            return Pos(self.x - other.x, self.y - other.y)
        elif isinstance(other, Size):
            return Pos(self.x - other.w, self.y - other.h)
        else:
            return NotImplemented

    def __mul__(self, other) -> 'Self':
        if isinstance(other, int):
            return Pos(self.x * other, self.y * other)
        else:
            return NotImplemented

class Size(object):
    """
    A 2D integer vector that represents a size.
    """

    def __init__(self, w: int, h: int):
        self.w, self.h = w, h

    def area(self) -> int:
        return self.w * self.h

    def __str__(self):
        return format('Size({0}, {1})', self.w, self.h)

    def __add__(self, other) -> 'Self':
        if isinstance(other, Size):
            return Size(self.w + other.w, self.w + other.h)
        elif isinstance(other, Pos):
            return Size(self.w + other.x, self.h + other.y)
        else:
            return NotImplemented

    def __sub__(self, other) -> 'Self':
        if isinstance(other, Size):
            return Size(self.w - other.w, self.h - other.h)
        elif isinstance(other, Pos):
            return Size(self.w - other.x, self.h - other.y)
        else:
            return NotImplemented

    def __mul__(self, other) -> 'Self':
        if isinstance(other, int):
            return Size(self.w * other, self.h * other)
        else:
            return NotImplemented

class Rect(object):
    """
    A 2D rectangle made with left up positon and size.
    """

    def __init__(self, x, y, w, h):
        self.pos: Pos = Pos(w, h)
        self.size: Size = Size(w, h)

    def __str__(self):
        return format('Rect({0}, {1}, {2}, {3})', self.x, self.y, self.w, self.h)

    def area(self) -> int:
        return self.size.area()

    def offset(self, pos: Pos) -> 'Self':
        return Rect(self.pos.x + pos.x, self.pos.y + pos.y, self.size.w, self.size.h)

    @staticmethod
    def from_vecs(pos: Pos, size: Size) -> 'Self':
        return Rect(pos.x, pos.y, size.w, size.h)

    @staticmethod
    def from_points(self, x1, y1, x2, y2) -> 'Self':
        return Rect(x1, y1, x2 - x1 + 1, y2 - y1 + 1)

    @staticmethod
    def from_point_vecs(self, left_up: Pos, right_down: Pos) -> 'Self':
        return Rect(left_up.x, left_up.y, right_down.x - left_up.x + 1, right_down.y - left_up + 1)

    def left_up(self) -> Pos:
        return self.pos

    def left_down(self) -> Pos:
        return Pos(self.pos.x, self.pos.y + self.size.h - 1)

    def right_up(self) -> Pos:
        return Pos(self.pos.x + self.size.w - 1, self.pos.y)

    def right_down(self) -> Pos:
        return Pos(self.pos.x + self.size.w - 1, self.pos.y + self.size.h - 1)

    def center(self) -> Pos:
        return Pos(self.pos.x + self.size.w // 2, self.pos.y + self.size.h // 2)
