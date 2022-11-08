import numpy as np
from typing import NamedTuple, Self

from .point import Point
from .axes import Axes
from .vector import Vector


class OrientedPoint(NamedTuple):
    """
    a named tuple that contains the information of position and orientation of an oriented point in 3D space

    Attributes
    ----------
    position : ~.entities.point.Point
        the position of the oriented point

    axes : ~.entities.axes.Axes
        the orientation of the oriented point
    """
    position: Point
    axes: Axes

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.position}, {self.axes})'

    def to_htm(self) -> np.ndarray:
        """
        transforms an oriented point instance to the homogeneous transformation matrix representation

        Returns
        -------
        out : np.ndarray
            the homogeneous transformation matrix as a np array
        """
        return np.array([[*self.axes.x, 0],
                         [*self.axes.y, 0],
                         [*self.axes.z, 0],
                         [*self.position, 1]]).T

    @classmethod
    def from_htm(cls, transformation_matrix: np.ndarray) -> Self:
        point: Point = Point(*transformation_matrix[0:3, 3])
        x: Vector = Vector(*transformation_matrix[0:3, 0])
        y: Vector = Vector(*transformation_matrix[0:3, 1])
        z: Vector = Vector(*transformation_matrix[0:3, 2])

        return cls(point, Axes(x, y, z))
