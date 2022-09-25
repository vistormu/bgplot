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
    def from_three_points(point1: Point, point2: Point, point3: Point):
        raise NotImplementedError()

    @staticmethod
    def from_line_and_point(line: Line, point: Point):
        raise NotImplementedError()
