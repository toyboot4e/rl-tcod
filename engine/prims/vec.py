from typing import Generator, Any, Tuple
from dataclasses import dataclass


@dataclass
class Pos(object):
    """A 2D immutable integer vector that represents a grid position.
    """
    x: int
    y: int

    def to_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def add(self, x: int, y: int) -> 'Pos':
        return Pos(self.x + x, self.y + y)

    def offset(self, offset: 'Pos') -> 'Pos':
        return Pos(self.x + offset.x, self.y + offset.y)

    def __str__(self):
        return 'Pos({0}, {1})'.format(self.x, self.y)

    def __add__(self, other: Any) -> 'Pos':
        if isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
        elif isinstance(other, Size):
            return Pos(self.x + other.w, self.y + other.h)
        else:
            return NotImplemented

    def __sub__(self, other: Any) -> 'Pos':
        if isinstance(other, Pos):
            return Pos(self.x - other.x, self.y - other.y)
        elif isinstance(other, Size):
            return Pos(self.x - other.w, self.y - other.h)
        else:
            return NotImplemented

    def __mul__(self, other: Any) -> 'Pos':
        if isinstance(other, int):
            return Pos(self.x * other, self.y * other)
        else:
            return NotImplemented


@dataclass
class Size(object):
    """A 2D immutable integer vector that represents a size.
    """

    w: int
    h: int

    def area(self) -> int:
        return self.w * self.h

    def to_tuple(self) -> Tuple[int, int]:
        return (self.w, self.h)

    def each(self) -> Generator[Tuple[int, int], None, None]:
        return ((x, y) for y in range(0, self.h) for x in range(0, self.w))

    def __str__(self):
        return format('Size({0}, {1})', self.w, self.h)

    def __add__(self, other: Any) -> 'Size':
        if isinstance(other, Size):
            return Size(self.w + other.w, self.w + other.h)
        elif isinstance(other, Pos):
            return Size(self.w + other.x, self.h + other.y)
        else:
            return NotImplemented

    def __sub__(self, other: Any) -> 'Size':
        if isinstance(other, Size):
            return Size(self.w - other.w, self.h - other.h)
        elif isinstance(other, Pos):
            return Size(self.w - other.x, self.h - other.y)
        else:
            return NotImplemented

    def __mul__(self, other: Any) -> 'Size':
        if isinstance(other, int):
            return Size(self.w * other, self.h * other)
        else:
            return NotImplemented


class Rect(object):
    """A 2D immutable rectangle made with left up positon and size.
    """

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.pos: Pos = Pos(x, y)
        self.size: Size = Size(w, h)

    def __str__(self) -> str:
        return 'Rect({}, {}, {}, {})'.format(self.pos.x, self.pos.y, self.size.w, self.size.h)

    def area(self) -> int:
        return self.size.area()

    def offset(self, pos: Pos) -> 'Rect':
        return Rect(self.pos.x + pos.x, self.pos.y + pos.y, self.size.w, self.size.h)

    @staticmethod
    def from_vecs(pos: Pos, size: Size) -> 'Rect':
        return Rect(pos.x, pos.y, size.w, size.h)

    @staticmethod
    def from_points(x1: int, y1: int, x2: int, y2: int) -> 'Rect':
        return Rect(x1, y1, x2 - x1 + 1, y2 - y1 + 1)

    @staticmethod
    def from_point_vecs(left_up: Pos, right_down: Pos) -> 'Rect':
        return Rect(left_up.x, left_up.y, right_down.x - left_up.x + 1, right_down.y - left_up.y + 1)

    def left_up(self) -> Pos:
        return self.pos

    def left_down(self) -> Pos:
        return Pos(self.pos.x, self.pos.y + self.size.h - 1)

    def right_up(self) -> Pos:
        return Pos(self.pos.x + self.size.w - 1, self.pos.y)

    def right_down(self) -> Pos:
        return Pos(self.pos.x + self.size.w - 1, self.pos.y + self.size.h - 1)

    def center(self) -> Pos:
        """Returns rounded center position."""
        return Pos(self.pos.x + self.size.w // 2, self.pos.y + self.size.h // 2)

    def left(self) -> int:
        return self.pos.x

    def right(self) -> int:
        return self.pos.x + self.size.w - 1

    def top(self) -> int:
        return self.pos.y

    def bottom(self) -> int:
        return self.pos.y + self.size.h - 1

    def intersects(self, other: 'Rect') -> bool:
        return not (self.right() < other.left() or self.left() > other.right()) and \
            not (self.bottom() < other.top() or self.top() > other.bottom())

    def each(self) -> Generator[Tuple[int, int], None, None]:
        return ((x, y) for y in range(self.top(), self.bottom() + 1) for x in range(self.left(), self.right() + 1))
