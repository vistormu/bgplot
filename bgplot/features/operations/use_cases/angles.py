import numpy as np

from ....entities import Vector


def get_angle_of_two_vectors(vector_1: Vector, vector_2: Vector, normal_vector: Vector, degrees: bool = False) -> float:
    v1: np.ndarray = np.array(vector_1.normalize())
    v2: np.ndarray = np.array(vector_2.normalize())
    n: np.ndarray = np.array(normal_vector.normalize())

    angle: float = np.arctan2(np.dot(np.cross(v2, v1), n), np.dot(v1, v2))

    if angle < 0.0:
        angle += 2.0*np.pi

    return angle if not degrees else angle*180/np.pi
