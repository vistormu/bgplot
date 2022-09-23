from typing import NamedTuple

from .vector import Vector


class Axes(NamedTuple):
    x: Vector
    y: Vector
    z: Vector
