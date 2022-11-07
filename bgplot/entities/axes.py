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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(({self.x.u}, {self.x.v}, {self.x.w}), ({self.y.u}, {self.y.v}, {self.y.w}), ({self.z.u}, {self.z.v}, {self.z.w}))'
