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
