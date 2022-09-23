from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float
    z: float

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):
        return Point(self.x*scalar, self.y*scalar, self.z*scalar)
