import numpy as np

from ..entities import Axes, Point, Vector, Plane, Line, ManipulatorData


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

    @staticmethod
    def get_transformations(a: list[float], d: list[float], alpha: list[float]):
        length: int = len(a)
        a_reversed: list[float] = list(reversed(a))
        d_reversed: list[float] = list(reversed(d))
        alpha_reversed: list[float] = list(reversed(alpha))

        z_axis_list: list[Vector] = []
        position_list: list[Point] = []

        for i in range(length):
            z_axis: np.ndarray = np.array([0,
                                           np.sin(alpha_reversed[i]),
                                           np.cos(alpha_reversed[i]),
                                           0]).round(4)

            position: np.ndarray = np.array([-a_reversed[i],
                                             -d_reversed[i] *
                                             np.sin(alpha_reversed[i]),
                                             -d_reversed[i] *
                                             np.cos(alpha_reversed[i]),
                                             1]).round(4)

            z_axis_list.append(z_axis)
            position_list.append(position)

        return z_axis_list, position_list

    @staticmethod
    def get_minimum_angle_vector(line: Line, vector: Vector):
        line_vector_1: np.ndarray = np.array([line.u, line.v, line.w])
        line_vector_2: np.ndarray = np.array([-line.u, -line.v, -line.w])
        z_axis: np.ndarray = np.array(vector)

        angle_1: float = np.arccos(np.dot(
            line_vector_1, z_axis)/(np.linalg.norm(line_vector_1)*np.linalg.norm(z_axis)))
        angle_2: float = np.arccos(np.dot(
            line_vector_2, z_axis)/(np.linalg.norm(line_vector_2)*np.linalg.norm(z_axis)))

        if angle_1 < angle_2:
            return Vector(*line_vector_1).normalize()
        else:
            return Vector(*line_vector_2).normalize()
