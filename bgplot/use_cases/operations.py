import numpy as np

from ..entities import Vector, Line, Point, Plane


def project_vector_on_plane(vector: Vector, plane: Plane) -> Vector:
    u: np.ndarray = np.array(vector)
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    v: np.ndarray = u - np.dot(u, n)*n

    v_vector: Vector = Vector(*v)

    return v_vector


def project_line_on_plane(line: Line, plane: Plane) -> Line:
    u: np.ndarray = np.array([line.u, line.v, line.w])
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    v: np.ndarray = u - np.dot(u, n)*n

    v_vector: Vector = Vector(*v)
    point: Point = Point(line.x, line.y, line.z)
    projected_line: Line = Line.from_vector_and_point(v_vector, point)

    return projected_line


def get_angle_of_two_vectors(vector_1: Vector, vector_2: Vector) -> float:
    u: np.ndarray = np.array(vector_1)
    v: np.ndarray = np.array(vector_2)

    angle: float = np.arccos(
        np.dot(u, v)/(np.linalg.norm(u)*np.linalg.norm(v)))

    return angle
