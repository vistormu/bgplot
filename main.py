import numpy as np

from src.core.logger import Logger
from src.entities import Point, Vector, Plane, ManipulatorData, Line, Axes
from src.use_cases import YamlRobotParser, ForwardKinematics, Graphics, ManipulatorDataGetter, InverseTransformation


def main():
    # ==================
    # INITIALIZATION
    # ==================
    log = Logger('main')

    # Manipulator
    manipulator_data: ManipulatorData = YamlRobotParser.to_manipulator_data(
        'ur3')
    manipulator_data.angles = [np.pi, 0.0, 0.0, 0.0, 0.0, np.pi/4]
    transformation_matrices: list[np.ndarray] = ForwardKinematics.get(
        manipulator_data)
    manipulator_data = ManipulatorDataGetter.get(
        transformation_matrices, manipulator_data)
    manipulator_data.positions.insert(0, Point(0.0, 0.0, 0.0))

    a: list[float] = manipulator_data.a_values.copy()
    d: list[float] = manipulator_data.d_values.copy()
    alpha: list[float] = manipulator_data.alpha_values.copy()
    positions: list[float] = manipulator_data.positions.copy()
    axes_list: list[Axes] = manipulator_data.axes_list.copy()
    axes_list.insert(0, Axes(Vector(1.0, 0.0, 0.0),
                             Vector(0.0, 1.0, 0.0),
                             Vector(0.0, 0.0, 1.0)))

    # Graphics
    graphics: Graphics = Graphics()
    graphics.set_limits(xlim=(-0.1, 0.7),
                        ylim=(-0.1, 0.5),
                        zlim=(0.0, 0.3))

    # Entities
    target: Point = positions[-1] + Point(0.1, 0.1, 0.1)
    target_axes: Axes = axes_list[-1]
    new_positions: list[Point] = [target]
    new_axes_list: list[Axes] = [target_axes]
    positions.pop()
    axes_list.pop()

    # ==================
    # IIK-ALGORITHM
    # ==================
    graphics.plot_points(positions, style='-o')
    graphics.plot_multiple_axes(axes_list, positions[1:])
    graphics.plot_points(new_positions, style='-o')
    graphics.plot_multiple_axes(new_axes_list, new_positions)

    graphics.show()
    graphics.clear()

    # 1. Calculate (i+1)z(i) and (i+1)p(i)
    relative_z_axes: list[np.ndarray] = None
    relative_positions: list[np.ndarray] = None
    relative_z_axes, relative_positions = InverseTransformation.get_transformations(a,
                                                                                    d,
                                                                                    alpha)

    for z, p in zip(relative_z_axes, relative_positions):
        log.debug(f'z: ({z[0]}, {z[1]}, {z[2]}), p: ({p[0]}, {p[1]}, {p[2]})')

    for i in range(manipulator_data.degrees_of_freedom):
        # 2. Calculate z(i) and p(i)
        transformation_matrix: np.ndarray = np.array([[*new_axes_list[i].x, 0],
                                                     [*new_axes_list[i].y, 0],
                                                     [*new_axes_list[i].z, 0],
                                                     [*new_positions[i], 1]]).T

        new_point_transformation: np.ndarray = transformation_matrix @ relative_positions[i].T
        p_i: Point = Point(*new_point_transformation[:-1])

        new_z_transformation: np.ndarray = transformation_matrix @ relative_z_axes[i].T
        z_i: Vector = Vector(*new_z_transformation[:-1]).normalize()

        positions.pop()
        axes_list.pop()

        # ==========
        graphics.plot_point(p_i)
        graphics.plot_vector(z_i, p_i, color='b')

        graphics.plot_points(positions, style='-o')
        graphics.plot_multiple_axes(axes_list, positions)
        graphics.plot_points(new_positions, style='-o')
        graphics.plot_multiple_axes(new_axes_list, new_positions)

        graphics.show()
        graphics.clear()
        # ==========

        # 3. Projected vector
        u_vector: Vector = Vector(*(p_i-positions[-1])).normalize()
        u: np.ndarray = np.array(u_vector)
        n: np.ndarray = np.array(z_i)
        v: np.ndarray = u - np.dot(u, n)*n

        # ==========
        v_vector: Vector = Vector(*v)
        line: Line = Line.from_two_points(p_i, positions[-1])
        line_projected: Line = Line.from_vector_and_point(v_vector, p_i)
        plane: Plane = Plane.from_normal_vector(z_i, p_i)

        graphics.plot_point(p_i)
        graphics.plot_vector(z_i, p_i, color='b')
        graphics.plot_vectors([v_vector, v_vector*-1.0], [p_i, p_i], color='r')
        graphics.plot_line(line, style='--', color='tab:gray')
        graphics.plot_line(line_projected, style='--', color='tab:gray')
        graphics.plot_plane(plane, p_i)

        graphics.plot_points(positions, style='-o')
        graphics.plot_multiple_axes(axes_list, positions)
        graphics.plot_points(new_positions, style='-o')
        graphics.plot_multiple_axes(new_axes_list, new_positions)

        graphics.show()
        graphics.clear()
        # ==========

        # 4. Least angle
        z: np.ndarray = np.array(axes_list[-1].z)
        angle_1: float = np.arccos(np.dot(v, z))
        angle_2: float = np.arccos(np.dot(-v, z))

        # Calculate y(i) or x(i)
        non_zero_vector: tuple(int) = (0 if abs(relative_positions[i+1][0]) < 0.001 else 1,
                                       0 if abs(
                                           relative_positions[i+1][1]) < 0.001 else 1,
                                       0 if abs(relative_positions[i+1][2]) < 0.001 else 1)

        if non_zero_vector == (0, 1, 0):
            if angle_1 < angle_2:
                y_i: Vector = Vector(*v).normalize()
            else:
                y_i: Vector = Vector(*-v).normalize()
        else:
            if angle_1 < angle_2:
                x_i: Vector = Vector(*v).normalize()
            else:
                x_i: Vector = Vector(*-v).normalize()

        # Calculate x(i) or y(i)
        if non_zero_vector == (0, 1, 0):
            x_i: Vector = Vector(*(np.cross(y_i, z_i))).normalize()
        else:
            y_i: Vector = Vector(*(np.cross(z_i, x_i))).normalize()

        # New position and axes
        axes_i: Axes = Axes(x_i, y_i, z_i)
        new_axes_list.append(axes_i)
        new_positions.append(p_i)

        # ==================
        # PLOTTING
        # ==================
        graphics.plot_points(positions, style='-o')
        graphics.plot_multiple_axes(axes_list, positions)
        graphics.plot_points(new_positions, style='-o')
        graphics.plot_multiple_axes(new_axes_list, new_positions)

        graphics.show()
        graphics.clear()


if __name__ == '__main__':
    main()
