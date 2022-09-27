from .point import Point
from .vector import Vector


class Line:
    def __init__(self, u: float, v: float, w: float, x: float, y: float, z: float) -> None:
        self.u: float = u
        self.v: float = v
        self.w: float = w
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(u: {self.u}, v: {self.v}, w: {self.w}, x: {self.x}, y: {self.y}, z: {self.z})'

    @staticmethod
    def from_two_points(point_1: Point, point_2: Point):
        vector: Vector = Vector(*(point_1-point_2))
        point: Point = (point_1+point_2)*0.5

        u: float = vector.u
        v: float = vector.v
        w: float = vector.w
        x: float = point.x
        y: float = point.y
        z: float = point.z

        return Line(u, v, w, x, y, z)

    @staticmethod
    def from_vector_and_point(vector: Vector, point: Point):
        u: float = vector.u
        v: float = vector.v
        w: float = vector.w
        x: float = point.x
        y: float = point.y
        z: float = point.z

        return Line(u, v, w, x, y, z)
