import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ..entities import Point, Vector, Plane, Line, Axes


class Graphics:
    def __init__(self) -> None:
        self._ax = plt.figure().add_subplot(111, projection='3d')

    def show(self) -> None:
        plt.show()

    def update(self, fps: int) -> None:
        plt.ion()
        plt.draw()
        plt.pause(1/fps)
        self._ax.cla()

    def close(self) -> None:
        plt.close()

    def clear(self) -> None:
        # self._ax.clear()
        plt.close()
        self._ax = plt.figure().add_subplot(111, projection='3d')
        self.set_limits(self.xlim, self.ylim, self.zlim)

    def set_limits(self, xlim: tuple[float], ylim: tuple[float], zlim: tuple[float]) -> None:
        self._ax.set_xlim(*xlim)
        self._ax.set_ylim(*ylim)
        self._ax.set_zlim(*zlim)

        self.xlim = xlim  # TMP
        self.ylim = ylim
        self.zlim = zlim

    def plot_points(self, points: list[Point], style: str = 'o', color: str = 'k') -> None:
        x: list[float] = [point.x for point in points]
        y: list[float] = [point.y for point in points]
        z: list[float] = [point.z for point in points]

        self._ax.plot(x, y, z, style, c=color)

    def plot_point(self, point: Point, color: str = 'r') -> None:
        self._ax.scatter(*point, c=color)

    def plot_oriented_point(self, point: Point, axes: Axes, length: float = 0.1, color: str = 'r') -> None:
        self._ax.scatter(*point, c=color)
        self.plot_axes(axes, point, length=length)

    def plot_vector(self, vector: Vector, position: Point, length: float = 0.1, color: str = 'b') -> None:
        color_dict: dict = {'r': (1.0, 0.0, 0.0),
                            'g': (0.0, 1.0, 0.0),
                            'b': (0.0, 0.0, 1.0),
                            'k': (0.0, 0.0, 0.0)}

        self._ax.quiver(position.x, position.y, position.z,
                        vector.u, vector.v, vector.w,
                        length=length,
                        colors=color_dict[color])

    def plot_vectors(self, vectors: list[Vector], positions: list[Point], length: float = 0.1, color: str = 'b') -> None:
        color_dict: dict = {'r': (1.0, 0.0, 0.0),
                            'g': (0.0, 1.0, 0.0),
                            'b': (0.0, 0.0, 1.0),
                            'k': (0.0, 0.0, 0.0)}

        x: list[float] = [position.x for position in positions]
        y: list[float] = [position.y for position in positions]
        z: list[float] = [position.z for position in positions]

        u: list[float] = [vector.u for vector in vectors]
        v: list[float] = [vector.v for vector in vectors]
        w: list[float] = [vector.w for vector in vectors]

        self._ax.quiver(z, y, z,
                        u, v, w,
                        length=length,
                        colors=color_dict[color])

    def plot_axes(self, axes: Axes, position: Point, length: float = 0.05) -> None:
        self._ax.quiver(position.x, position.y, position.z,
                        axes.x.u, axes.x.v, axes.x.w,
                        length=length,
                        colors=(1.0, 0.0, 0.0))

        self._ax.quiver(position.x, position.y, position.z,
                        axes.y.u, axes.y.v, axes.y.w,
                        length=length,
                        colors=(0.0, 1.0, 0.0))

        self._ax.quiver(position.x, position.y, position.z,
                        axes.z.u, axes.z.v, axes.z.w,
                        length=length,
                        colors=(0.0, 0.0, 1.0))

    def plot_multiple_axes(self, axes_list: list[Axes], positions: list[Point], length: float = 0.05) -> None:
        for axes, position in zip(axes_list, positions):
            self.plot_axes(axes, position, length=length)

    def plot_line(self, line: Line, line_range: tuple[float] = (-2.0, 2.0), style: str = '-', color: str = 'k') -> None:
        t: np.ndarray = np.linspace(*line_range)
        x: np.ndarray = np.array(line.x + t*line.a)
        y: np.ndarray = np.array(line.y + t*line.b)
        z: np.ndarray = np.array(line.z + t*line.c)

        self._ax.plot(x, y, z, style, c=color)

    def plot_plane(self, plane: Plane, center: Point, size: float = 0.2, alpha: float = 0.5) -> None:
        linspace: np.ndarray = np.linspace(-size, size, 2)
        meshgrid: list[np.ndarray] = np.meshgrid(linspace, linspace)

        non_zero_vector: tuple(int) = (0 if abs(plane.a) < 0.01 else 1,
                                       0 if abs(plane.b) < 0.01 else 1,
                                       0 if abs(plane.c) < 0.01 else 1)

        match(non_zero_vector):
            case (0, 0, 1):
                plane_x: np.ndarray = meshgrid[0] + center.x
                plane_y: np.ndarray = meshgrid[1] + center.y
                plane_z: np.ndarray = np.zeros_like(plane_x) - plane.d
            case (0, 1, 0):
                plane_x: np.ndarray = meshgrid[0] + center.x
                plane_z: np.ndarray = meshgrid[1] + center.z
                plane_y: np.ndarray = np.zeros_like(plane_x) - plane.d
            case (0, 1, 1):
                plane_x: np.ndarray = meshgrid[0] + center.x
                plane_z: np.ndarray = meshgrid[1] + center.z
                plane_y: np.ndarray = (-plane.d - plane.c*plane_z)/plane.b
            case (1, 0, 0):
                plane_y: np.ndarray = meshgrid[0] + center.y
                plane_z: np.ndarray = meshgrid[1] + center.z
                plane_x: np.ndarray = np.zeros_like(plane_y) - plane.d
            case (1, 0, 1):
                plane_x: np.ndarray = meshgrid[0] + center.x
                plane_y: np.ndarray = meshgrid[1] + center.y
                plane_z: np.ndarray = (-plane.d - plane.a*plane_x)/plane.b
            case (1, 1, 0):
                plane_x: np.ndarray = meshgrid[0] + center.x
                plane_z: np.ndarray = meshgrid[1] + center.z
                plane_y: np.ndarray = (-plane.d - plane.a*plane_x)/plane.b
            case (1, 1, 1):
                plane_x: np.ndarray = meshgrid[0] + center.x
                plane_y: np.ndarray = meshgrid[1] + center.y
                plane_z: np.ndarray = (-plane.d - plane.a *
                                       plane_x - plane.b*plane_y)/plane.c

        self._ax.plot_surface(plane_x, plane_y, plane_z, alpha=alpha)
