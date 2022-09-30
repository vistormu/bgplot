import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ...entities import Point, Vector, Plane, Line, Axes
from .use_cases import point_plotting


class Graphics:
    def __init__(self, size: int = 200) -> None:
        self.size: int = size
        self.init()

    def init(self):
        # Figure variables
        self.title: str = ''
        self.limits_set: bool = False
        self.lock_aspect_ratio: bool = True
        self.x_limits: tuple[float] = None
        self.y_limits: tuple[float] = None
        self.z_limits: tuple[float] = None

        # Figure
        figure = plt.figure(dpi=self.size)
        self._ax = figure.add_subplot(111, projection='3d')

        # Methods
        self.set_title(self.title)
        if self.limits_set:
            self.set_limits(self.x_limits,
                            self.y_limits,
                            self.z_limits,
                            self.lock_aspect_ratio)

    def set_title(self, title: str):
        self.title = title
        self._ax.set_title(title)

    def show(self) -> None:
        plt.show()
        self.clear()

    def update(self, fps: int) -> None:
        plt.ion()
        plt.draw()
        plt.pause(1/fps)
        self._ax.cla()

    def close(self) -> None:
        plt.close()

    def clear(self) -> None:
        self._ax.clear()
        plt.close()
        self.init()

    def set_limits(self, xlim: tuple[float], ylim: tuple[float], zlim: tuple[float], lock_aspect_ratio: bool = True) -> None:
        self.x_limits = xlim
        self.y_limits = ylim
        self.z_limits = zlim

        self.lock_aspect_ratio = lock_aspect_ratio

        # Set limits
        self._ax.set_xlim(*xlim)
        self._ax.set_ylim(*ylim)
        self._ax.set_zlim(*zlim)

        # Set aspect ratio
        if self.lock_aspect_ratio:
            ratio: float = xlim[1]-xlim[0]
            self._ax.set_box_aspect(aspect=(1.0,
                                            (ylim[1]-ylim[0])/ratio,
                                            (zlim[1]-zlim[0])/ratio))

    # ==========
    # POINTS
    # ==========
    def add_point(self, point: Point, color: str = 'k') -> None:
        """
        Description

        Parameters
        ----------
        arg1 : type
            description

        See Also
        --------
        function : description
        """
        point_plotting.add_point(self._ax, point, color)

    def add_points(self, points: list[Point], style: str = 'o', color: str = 'k') -> None:
        """
        Description

        Parameters
        ----------
        arg1 : type
            description

        See Also
        --------
        function : description
        """
        point_plotting.add_points(self._ax, points, style, color)

    def add_oriented_point(self, point: Point, axes: Axes, length: float = 0.025, color: str = 'k') -> None:
        self._ax.scatter(*point, c=color)
        self.add_axes(axes, point, length=length)

    def add_oriented_points(self, points: list[Point], axes_list: list[Axes], style: str = 'o', length: float = 0.025, color: str = 'k') -> None:
        """
        Description

        Parameters
        ----------
        arg1 : type
            description

        See Also
        --------
        function : description
        """
        assert len(points) == len(axes_list)

        point_plotting.add_oriented_points(
            self._ax, points, axes_list, style, length, color)

    # ==========
    # VECTORS
    # ==========

    def add_vector(self, vector: Vector, position: Point = Point(0.0, 0.0, 0.0), length: float = 0.025, color: str = 'b') -> None:
        color_dict: dict = {'r': (1.0, 0.0, 0.0),
                            'g': (0.0, 1.0, 0.0),
                            'b': (0.0, 0.0, 1.0),
                            'k': (0.0, 0.0, 0.0)}

        self._ax.quiver(position.x, position.y, position.z,
                        vector.u, vector.v, vector.w,
                        length=length,
                        colors=color_dict[color])

    def add_vectors(self, vectors: list[Vector], positions: list[Point], length: float = 0.025, color: str = 'b') -> None:
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

        self._ax.quiver(x, y, z,
                        u, v, w,
                        length=length,
                        colors=color_dict[color])

    def add_axes(self, axes: Axes, position: Point, length: float = 0.025) -> None:
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

    def add_multiple_axes(self, axes_list: list[Axes], positions: list[Point], length: float = 0.05) -> None:
        for axes, position in zip(axes_list, positions):
            self.add_axes(axes, position, length=length)

    def add_line(self, line: Line, line_range: tuple[float] = (-2.0, 2.0), style: str = '-', color: str = 'k') -> None:
        t: np.ndarray = np.linspace(*line_range)
        x: np.ndarray = np.array(line.x + t*line.u)
        y: np.ndarray = np.array(line.y + t*line.v)
        z: np.ndarray = np.array(line.z + t*line.w)

        self._ax.plot(x, y, z, style, c=color)

    def add_plane(self, plane: Plane, center: Point = Point(0.0, 0.0, 0.0), size: float = 0.2, alpha: float = 0.5) -> None:
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
                plane_z: np.ndarray = (-plane.d - plane.a*plane_x)/plane.c
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
