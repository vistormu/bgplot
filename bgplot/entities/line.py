from typing import Self

from .point import Point
from .vector import Vector


class Line:
    """
    a class that contains the information of a 3D Line: (x, y, z) + t(u, v, w)

    Attributes
    ----------
    u : float
        the u value of the director vector of the line

    v : float
        the v value of the director vector of the line

    w : float
        the w value of the director vector of the line

    x: float
         the x value of the point contained in the line

    y: float
         the y value of the point contained in the line

    z: float
         the z value of the point contained in the line
    """

    def __init__(self, u: float, v: float, w: float, x: float, y: float, z: float) -> None:
        self.u: float = u
        self.v: float = v
        self.w: float = w
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(u: {self.u}, v: {self.v}, w: {self.w}, x: {self.x}, y: {self.y}, z: {self.z})'

    @classmethod
    def from_two_points(cls, point_1: Point, point_2: Point) -> Self:
        """
        creates a Line instance given two points

        Arguments
        ---------
        point_1 : ~.entities.point.Point
            the first point

        point_2 : ~.entities.point.Point
            the second point

        Returns
        -------
        out : ~.entities.line.Line
            the line given by two points
        """
        vector: Vector = Vector(*(point_1-point_2))
        point: Point = (point_1+point_2)*0.5

        u: float = vector.u
        v: float = vector.v
        w: float = vector.w
        x: float = point.x
        y: float = point.y
        z: float = point.z

        return cls(u, v, w, x, y, z)

    @classmethod
    def from_vector_and_point(cls, vector: Vector, point: Point) -> Self:
        """
        creates a Line instance given a director vector and a point

        Arguments
        ---------
        vector : ~.entities.vector.Vector
            the director vector of the line

        point : ~.entities.point.Point
            a point contained in the line

        Returns
        -------
        out : ~.entities.line.Line
            the line given by the director vector and the point
        """
        u: float = vector.u
        v: float = vector.v
        w: float = vector.w
        x: float = point.x
        y: float = point.y
        z: float = point.z

        return cls(u, v, w, x, y, z)
