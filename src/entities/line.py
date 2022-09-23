from .point import Point
from .vector import Vector


class Line:
    def __init__(self, a: float, b: float, c: float, x: float, y: float, z: float) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(a: {self.a}, b: {self.b}, c: {self.c}, x: {self.x}, y: {self.y}, z: {self.z})'

    @staticmethod
    def from_two_points(point_1: Point, point_2: Point):
        vector: Vector = Vector(*(point_1-point_2))
        point: Point = (point_1+point_2)*0.5

        a: float = vector.u
        b: float = vector.v
        c: float = vector.w
        x: float = point.x
        y: float = point.y
        z: float = point.z

        return Line(a, b, c, x, y, z)
