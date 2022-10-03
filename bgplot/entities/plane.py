import numpy as np

from ..entities import Point, Vector, Line


class Plane:
    """
    a class that contains information about the mathematical representation of a plane: ax+by+cz+d = 0

    Attributes
    ----------
    a : float
        "a" coefficient of the plane equation

    b : float
        "b" coefficient of the plane equation

    c : float
        "c" coefficient of the plane equation

    d : float
        "d" constant of the plane equation
    """

    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c
        self.d: float = d

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d})'

    @staticmethod
    def from_normal_vector_and_point(vector: Vector, point: Point):
        """
        creates a plane from a normal vector and a point

        Arguments
        ---------
        vector : ~.entities.vector.Vector
            the normal vector of the plane

        point : ~.entities.point.Point
            a point contained on the plane

        Returns
        -------
            out : ~.entities.plane.Plane

        Raises
        ------
        ValueError
            if the normal vector has no dimension
        """
        if vector == Vector(0.0, 0.0, 0.0):
            raise ValueError('cannot instantiate plane with null vector')

        a: float = vector.u
        b: float = vector.v
        c: float = vector.w
        d: float = -vector.u*point.x - vector.v*point.y - vector.w*point.z

        return Plane(a, b, c, d)

    @staticmethod
    def from_three_points(point_1: Point, point_2: Point, point_3: Point):
        """
        creates a plane given three different points

        Arguments
        ---------
        point_1 : ~.entities.point.Point
            the first point

        point_2 : ~.entities.point.Point
            the second point

        point_3 : ~.entities.point.Point
            the third point

        Returns
        -------
        out : ~.entities.plane.Plane
            the plane formed by the three given points
        """
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
        """
        creates a plane from a line and a point

        Arguments
        ---------
        line : ~.entities.line.Line
            the line contained on the plane

        point : ~.entities.point.Point
            the point contained on the plane

        Returns
        -------
        out : ~.entities.plane.Plane
            the plane formed given by the line and the point
        """
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
    def from_two_vectors_and_point(vector_1: Vector, vector_2: Vector, point: Point):
        """
        creates a plane from two vectors and a point

        Arguments
        ---------
        vector_1 : ~.entities.vector.Vector
            the first vector contained on the plane

        vector_2 : ~.entities.vector.Vector
            the second vector contained on the plane

        point : ~.entities.point.Point
            the point contained on the plane

        Returns
        -------
        out : ~.entities.plane.Plane
            the plane formed by the given vectors and point

        Raises
        ------
        ValueError
            if any of the given vectors has no dimensions
        """
        if vector_1 == Vector(0.0, 0.0, 0.0) or vector_2 == Vector(0.0, 0.0, 0.0):
            raise ValueError('cannot instantiate plane with null vector')

        normal_vector = Vector(*np.cross(vector_1, vector_2)).normalize()

        a: float = normal_vector.u
        b: float = normal_vector.v
        c: float = normal_vector.w
        d: float = -normal_vector.u*point.x - \
            normal_vector.v*point.y - normal_vector.w*point.z

        return Plane(a, b, c, d)
