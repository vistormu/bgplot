import numpy as np

from ....entities import Point, Line, Plane


def get_intersection_of_line_and_plane(line: Line, plane: Plane) -> Point:
    v: np.ndarray = np.array([line.u, line.v, line.w])
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    line_point: np.ndarray = np.array([line.x, line.y, line.z])

    dot_product: float = np.dot(n, v)

    if abs(dot_product) < 0.01:
        raise ValueError('the plane and the line are parallel to each other')

    t: float = -(plane.d+np.dot(n, line_point))/dot_product

    intersection_point: Point = Point(*(line_point + v*t))

    return intersection_point
