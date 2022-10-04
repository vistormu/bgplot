import numpy as np

from ....entities import Point, Vector, Line, Plane
from .intersections import get_intersection_of_line_and_plane


def project_vector_on_plane(vector: Vector, plane: Plane) -> Vector:
    u: np.ndarray = np.array(vector)
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    v: np.ndarray = u - np.dot(u, n)/np.power(np.linalg.norm(n), 2)*n

    v_vector: Vector = Vector(*v)

    return v_vector


def project_line_on_plane(line: Line, plane: Plane) -> Line:
    u: np.ndarray = np.array([line.u, line.v, line.w])
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    v: np.ndarray = u - np.dot(u, n)/np.power(np.linalg.norm(n), 2)*n

    point: Point = get_intersection_of_line_and_plane(line, plane)
    projected_line: Line = Line.from_vector_and_point(Vector(*v), point)

    return projected_line
