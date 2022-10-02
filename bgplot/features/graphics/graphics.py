import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ...entities import Point, Vector, Plane, Line, Axes
from .use_cases import point_plotting, vector_plotting, axes_plotting, line_plotting, plane_plotting


class Graphics:
    def __init__(self, size: int = 200) -> None:
        self.size: int = size
        self.init()

    def init(self):
        # Figure variables
        self._title: str = ''
        self.limits_set: bool = False
        self.lock_aspect_ratio: bool = True
        self.x_limits: tuple[float] = None
        self.y_limits: tuple[float] = None
        self.z_limits: tuple[float] = None

        # Figure
        figure = plt.figure(dpi=self.size)
        self._ax = figure.add_subplot(111, projection='3d')

        # Methods
        self.set_title(self._title)
        if self.limits_set:
            self.set_limits(self.x_limits,
                            self.y_limits,
                            self.z_limits,
                            self.lock_aspect_ratio)

    def set_title(self, title: str):
        self._title = title
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
        point_plotting.add_oriented_point(self._ax, point, axes, length, color)

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
    def add_vector(self, vector: Vector, position: Point = Point(0.0, 0.0, 0.0), length: float = 0.025, color: str = 'k') -> None:
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

        vector_plotting.add_vector(self._ax, vector, position, length, color)

    def add_vectors(self, vectors: list[Vector], positions: list[Point], length: float = 0.025, color: str = 'k') -> None:
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
        assert len(vectors) == len(positions)

        vector_plotting.add_vectors(
            self._ax, vectors, positions, length, color)

    # ==========
    # AXES
    # ==========
    def add_axes(self, axes: Axes, position: Point = Point(0.0, 0.0, 0.0), length: float = 0.025) -> None:
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
        axes_plotting.add_axes(self._ax, axes, position, length)

    def add_multiple_axes(self, axes_list: list[Axes], positions: list[Point], length: float = 0.05) -> None:
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
        assert len(axes_list) == len(positions)

        axes_plotting.add_multiple_axes(self._ax, axes_list, positions, length)

    # ==========
    # LINES
    # ==========
    def add_line(self, line: Line, line_range: tuple[float] = (-2.0, 2.0), style: str = '-', color: str = 'k') -> None:
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
        line_plotting.add_line(self._ax, line, line_range, style, color)

    def add_lines(self, lines: list[Line], line_range: tuple[float] = (-2.0, 2.0), style: str = '-', color: str = 'k') -> None:
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
        line_plotting.add_lines(self._ax, lines, line_range, style, color)

    # ==========
    # PLANES
    # ==========
    def add_plane(self, plane: Plane, center: Point = Point(0.0, 0.0, 0.0), size: float = 0.2, alpha: float = 0.5) -> None:
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
        plane_plotting.add_plane(self._ax, plane, center, size, alpha)

    def add_planes(self, planes: list[Plane], centers: list[Point], size: float = 0.2, alpha: float = 0.5) -> None:
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
        assert len(planes) == len(centers)

        plane_plotting.add_planes(self._ax, planes, centers, size, alpha)
