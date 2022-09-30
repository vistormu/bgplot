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


def get_angle_of_two_vectors(vector_1: Vector, vector_2: Vector, normal_vector: Vector) -> float:
    v1: np.ndarray = np.array(vector_1.normalize())
    v2: np.ndarray = np.array(vector_2.normalize())
    n: np.ndarray = np.array(normal_vector.normalize())

    angle: float = np.arctan2(np.dot(np.cross(v2, v1), n), np.dot(v1, v2))

    if angle < 0.0:
        angle += 2.0*np.pi

    return angle


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
