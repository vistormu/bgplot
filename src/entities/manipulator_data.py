from dataclasses import dataclass

from .point import Point
from .vector import Vector
from .axes import Axes


@dataclass
class ManipulatorData:
    name: str
    a_values: list[float]
    d_values: list[float]
    alpha_values: list[float]
    lengths: list[float]
    degrees_of_freedom: int
    positions: list[Point]
    angles: list[float]
    x_vectors: list[Vector]
    y_vectors: list[Vector]
    z_vectors: list[Vector]
    axes_list: list[Axes]
