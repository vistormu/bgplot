import numpy as np

from ..entities import Axes, Point, Vector


class InverseTransformation:
    @staticmethod
    def get_position(position: Point, axes: Axes, a: float, d: float, alpha: float):
        transformation_matrix: np.ndarray = np.array([[*axes.x, 0],
                                                     [*axes.y, 0],
                                                     [*axes.z, 0],
                                                     [*position, 1]]).T

        translation_vector: np.ndarray = np.array(
            [-a, -d*np.sin(alpha), -d*np.cos(alpha), 1]).T

        new_point = transformation_matrix @ translation_vector
        new_point = Point(*new_point[:-1])

        return new_point

    @staticmethod
    def get_z_axis(position: Point, axes: Axes, alpha: float):
        transformation_matrix: np.ndarray = np.array([[*axes.x, 0],
                                                     [*axes.y, 0],
                                                     [*axes.z, 0],
                                                     [*position, 1]]).T

        translation_vector: np.ndarray = np.array(
            [0, np.sin(alpha), np.cos(alpha), 0]).T

        new_vector = transformation_matrix @ translation_vector
        new_vector = Vector(*new_vector[:-1])

        return new_vector
