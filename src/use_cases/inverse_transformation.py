import numpy as np

from ..entities import Axes, Point, Vector, Plane, Line


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

    @staticmethod
    def get_projection(plane: Plane, line: Line, point: Point):
        u: np.ndarray = np.array([line.u, line.v, line.w])
        n: np.ndarray = np.array([plane.a, plane.b, plane.c])

        projected_vector: np.ndarray = u - \
            (u*n.T)/np.power(np.linalg.norm(n), 2)*n

        line: Line = Line.from_vector_and_point(
            Vector(*projected_vector), point)

        return line
