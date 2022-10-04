import numpy as np

from ....entities import Point


def distance_between_two_points(point_1: Point, point_2: Point) -> float:
    distance: float = np.linalg.norm(point_1-point_2)

    return distance
