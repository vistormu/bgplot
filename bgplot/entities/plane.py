import numpy as np

from ..entities import Point, Vector, Line


class Plane:
    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c
        self.d: float = d

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d})'

    @staticmethod
    def from_normal_vector(vector: Vector, point: Point):
        a: float = vector.u
        b: float = vector.v
        c: float = vector.w
        d: float = -vector.u*point.x - vector.v*point.y - vector.w*point.z

        return Plane(a, b, c, d)

    @staticmethod
    def from_three_points(point_1: Point, point_2: Point, point_3: Point):
        vector_1: Vector = Vector(*(point_1-point_2)).normalize()
        vector_2: Vector = Vector(*(point_1-point_3)).normalize()
        normal_vector = Vector(*np.cross(vector_1, vector_2)).normalize()

        a: float = normal_vector.u
        b: float = normal_vector.v
        c: float = normal_vector.w
        d: float = -normal_vector.u*point_1.x - \
            normal_vector.v*point_1.y - normal_vector.w*point_1.z

        return Plane(a, b, c, d)

    @staticmethod
    def from_line_and_point(line: Line, point: Point):
        vector_1: Vector = Vector(line.u, line.v, line.w).normalize()
        vector_2: Vector = Vector(
            *(point-Point(line.x, line.y, line.z))).normalize()
        normal_vector = Vector(*np.cross(vector_1, vector_2)).normalize()

        a: float = normal_vector.u
        b: float = normal_vector.v
        c: float = normal_vector.w
        d: float = -normal_vector.u*point.x - \
            normal_vector.v*point.y - normal_vector.w*point.z

        return Plane(a, b, c, d)

    @staticmethod
    def from_two_vectors(vector_1: Vector, vector_2: Vector, point: Point):
        normal_vector = Vector(*np.cross(vector_1, vector_2)).normalize()

        a: float = normal_vector.u
        b: float = normal_vector.v
        c: float = normal_vector.w
        d: float = -normal_vector.u*point.x - \
            normal_vector.v*point.y - normal_vector.w*point.z

        return Plane(a, b, c, d)
