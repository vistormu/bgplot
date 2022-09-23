import yaml

from ..entities import ManipulatorData,  Point, Vector, Axes

ASSETS_PATH = 'src/assets/'


class YamlRobotParser:
    @staticmethod
    def to_manipulator_data(robot: str) -> ManipulatorData:
        path: str = ASSETS_PATH + robot + '.yaml'

        with open(path, "r") as file:
            try:
                dh_table = yaml.safe_load(file)
            except yaml.YAMLError as exception:
                print(exception)

        name: str = robot
        a_values: list[float] = dh_table[robot]['a']
        d_values: list[float] = dh_table[robot]['d']
        alpha_values: list[float] = dh_table[robot]['alpha']
        lengths: list[float] = [abs(sum(x)) for x in zip(a_values, d_values)]
        degrees_of_freedom: int = len(a_values)
        angles: list[float] = [0.0]*degrees_of_freedom
        positions: list[Point] = [Point(0.0, 0.0, 0.0)]*degrees_of_freedom
        x_vectors: list[Vector] = [Vector(0.0, 0.0, 0.0)]*degrees_of_freedom
        y_vectors: list[Vector] = [Vector(0.0, 0.0, 0.0)]*degrees_of_freedom
        z_vectors: list[Vector] = [Vector(0.0, 0.0, 0.0)]*degrees_of_freedom
        axes_list: list[Axes] = [
            Axes(*axes) for axes in zip(x_vectors, y_vectors, z_vectors)]

        manipulator_data: ManipulatorData = ManipulatorData(name=name,
                                                            a_values=a_values,
                                                            d_values=d_values,
                                                            alpha_values=alpha_values,
                                                            lengths=lengths,
                                                            degrees_of_freedom=degrees_of_freedom,
                                                            positions=positions,
                                                            angles=angles,
                                                            x_vectors=x_vectors,
                                                            y_vectors=y_vectors,
                                                            z_vectors=z_vectors,
                                                            axes_list=axes_list)

        return manipulator_data
