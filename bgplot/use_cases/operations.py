import numpy as np

from ..core.logger import Logger
from ..entities import Vector, Line, Point, Plane


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


def get_angle_of_two_vectors(vector_1: Vector, vector_2: Vector, radians: bool = True) -> float:
    angle: float = np.arctan2(vector_1.v, vector_1.u) - \
        np.arctan2(vector_2.v, vector_2.u)

    if angle < 0:
        angle += 2*np.pi

    return angle if radians else angle*180/np.pi


def get_intersection_of_line_and_plane(line: Line, plane: Plane) -> Point:
    v: np.ndarray = np.array([line.u, line.v, line.w])
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    line_point: np.ndarray = np.array([line.x, line.y, line.z])

    dot_product: float = np.dot(n, v)

    if abs(dot_product) < 0.01:
        Logger.error('The line and the plane are parallel to each other.')
        # WIP
        return

    t: float = -(plane.d+np.dot(n, line_point))/dot_product

    intersection_point: Point = Point(*(line_point + v*t))

    return intersection_point
