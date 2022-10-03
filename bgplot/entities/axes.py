from typing import NamedTuple

from .vector import Vector


class Axes(NamedTuple):
    """
    a named tuple that contains the information of three vectors that form a group of axis

    Attributes
    ----------
    x : ~.entities.vector.Vector
        the x axis

    y : ~.entities.vector.Vector
        the y axis

    z : ~.entities.vector.Vector
        the z axis
    """
    x: Vector
    y: Vector
    z: Vector
