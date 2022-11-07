import numpy as np
from typing import NamedTuple

from .point import Point
from .axes import Axes


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

    def to_homogeneous_transformation_matrix(self) -> np.ndarray:
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
