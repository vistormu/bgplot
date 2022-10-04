import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ...entities import Point, Vector, Plane, Line, Axes
from .use_cases import point_plotting, vector_plotting, axes_plotting, line_plotting, plane_plotting


class Graphics:
    """
    the ~.Graphics class includes the graphical representation of all the bgplot's entities
    """

    def __init__(self, size: int = 200) -> None:
        self.size: int = size
        self.limits_set: bool = False
        self.view_set: bool = False
        self.azimut: float = 0.0
        self.elevation: float = 0.0
        self.lock_aspect_ratio: bool = True
        self._title: str = ''
        self.x_limits: tuple[float] = None
        self.y_limits: tuple[float] = None
        self.z_limits: tuple[float] = None
        self._recreate_figure()

    def _recreate_figure(self) -> None:
        figure = plt.figure(dpi=self.size)
        self._ax = figure.add_subplot(111, projection='3d')

    def _reset_methods(self) -> None:
        self.set_title(self._title)
        if self.limits_set:
            self.set_limits(self.x_limits,
                            self.y_limits,
                            self.z_limits,
                            self.lock_aspect_ratio)

        if self.view_set:
            self.set_view(self.azimut, self.elevation)

    def _update_reset_methods(self) -> None:
        self.set_title(self._title)
        if self.limits_set:
            self.set_limits(self.x_limits,
                            self.y_limits,
                            self.z_limits,
                            self.lock_aspect_ratio)

    def set_title(self, title: str) -> None:
        """
        sets the title for the next figures

        Parameters
        ----------
        title : str
            the title to be set
        """
        self._title = title
        self._ax.set_title(title)

    def show(self) -> None:
        """
        displays all the added entities

        Notes
        -----
        after showing the figure, it will be cleared

        See Also
        --------
        update : updates the figure for interactive plotting
        """
        plt.show()
        self.clear()

    def update(self, fps: int) -> None:
        """
        updates the figure for interactive plotting

        Parameters
        ----------
        fps : int
            the frames per second to update the display

        See Also
        --------
        show : displays all the added entities
        """
        plt.ion()
        plt.draw()
        plt.pause(1/fps)
        self._ax.cla()
        self._update_reset_methods()

    def close(self) -> None:
        """
        closes the figure window
        """
        plt.close()

    def clear(self) -> None:
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
        self._ax.clear()
        plt.close()
        self._recreate_figure()
        self._reset_methods()

    def set_limits(self, xlim: tuple[float], ylim: tuple[float], zlim: tuple[float], lock_aspect_ratio: bool = True) -> None:
        """
        sets the limits of each axis of the figure

        Parameters
        ----------
        xlim : tuple[float]
            the limits of the x axis

        ylim : tuple[float]
            the limits of the y axis

        zlim : tuple[float]
            the limits of the z axis

        lock_aspect_ratio : bool, optional
            locks the aspect ratio of the figure so the length of all axes are consistent. True by default
        """
        self.x_limits = xlim
        self.y_limits = ylim
        self.z_limits = zlim

        self.limits_set = True
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

    def set_view(self, azimut: float, elevation: float) -> None:
        """
        sets the viewing angle given the azimut and the elevation

        Arguments
        ---------
        azimut : float
            the azimut angle

        elevation : float
            the elevation angle
        """
        self.view_set = True
        self.azimut = azimut
        self.elevation = elevation

        self._ax.view_init(elev=elevation, azim=azimut)

    # ==========
    # POINTS
    # ==========
    def add_point(self, point: Point, color: str = 'k') -> None:
        """
        adds a point to be displayed

        Parameters
        ----------
        point : ~.entities.point.Point
            the point to be added

        color : str, optional
            the color of the point. Uses the same notation as matplotlib's color code. 'k' (black) by default

        See Also
        --------
        add_points : adds multiple points to be displayed
        add_oriented_point : adds a point with orientation to be displayed
        add_oriented_points : adds multiple points with orientation to be displayed
        """
        point_plotting.add_point(self._ax, point, color)

    def add_points(self, points: list[Point], style: str = 'o', color: str = 'k') -> None:
        """
        adds multiple points to be displayed

        Parameters
        ----------
        points : list[~.entities.point.Point]
            the list of points to be added

        style : str, optional
            the style of the line that joins the points. Uses the same notation as matplotlib's style code. 'o' by default

        color : str, optional
            the color of the points. Uses the same notation as matplotlib's color code. 'k' (black) by default

        See Also
        --------
        add_point : adds a point to be displayed
        add_oriented_point : adds a point with orientation to be displayed
        add_oriented_points : adds multiple points with orientation to be displayed
        """
        point_plotting.add_points(self._ax, points, style, color)

    def add_oriented_point(self, point: Point, axes: Axes, length: float = 0.025, color: str = 'k') -> None:
        """
        adds a point with orientation to be displayed

        Parameters
        ----------
        point : ~.entities.point.Point
            the point to be added

        axes : ~.entities.axes.Axes
            the orientation of the point given by the axes

        length : float, optional
            the length of the displayed axes. 0.025 by default

        color : str, optional
            the color of the point. 'k' (black) by default

        Notes
        -----
        the color of the axes are given by the standard x-red, y-green, z-blue

        See Also
        --------
        add_point : adds a point to be displayed
        add_points : adds multiple points to be displayed
        add_oriented_points : adds multiple points with orientation to be displayed
        """
        point_plotting.add_oriented_point(self._ax, point, axes, length, color)

    def add_oriented_points(self, points: list[Point], axes_list: list[Axes], style: str = 'o', length: float = 0.025, color: str = 'k') -> None:
        """
        adds multiple points with orientation to be displayed

        Parameters
        ----------
        points : list[~.entities.point.Point]
            the points to be added

        axes_list : list[~.entities.axes.Axes]
            the orientation of each point

        style : str, optional
            the line style of the connection of points. Follows the matplotlib's style code. 'o' by default

        length : float, optional
            the length of the displayed axes. 0.025 by default

        color : str, optional
            the color of the points. 'k' (black) by default

        Raises
        ------
        IndexError
            if the lengths of the point and axes list do not match

        Notes
        -----
        the color of the axes are given by the standard x-red, y-green, z-blue

        See Also
        --------
        add_point : adds a point to be displayed
        add_points : adds multiple points to be displayed
        add_oriented_point : adds a point with orientation to be displayed
        """
        if len(points) != len(axes_list):
            raise IndexError(
                'the lengths of the points and axes list does not match')

        point_plotting.add_oriented_points(
            self._ax, points, axes_list, style, length, color)

    # ==========
    # VECTORS
    # ==========
    def add_vector(self, vector: Vector, position: Point = Point(0.0, 0.0, 0.0), length: float = 0.025, color: str = 'k') -> None:
        """
        add a vector to be displayed

        Parameters
        ----------
        vector : ~.entities.vector.Vector
            the vector to be displayed

        position : ~.entities.point.Point, optional
            the position of the vector. On the origin by default

        length : float, optional
            the length of the displayed vector. 0.025 by default

        color : str, optional
            the color of the plotted vector. 'k' black by default. Currently only supports 'k' (black), 'r' (red), 'g' (green) and 'b' (blue)

        Notes
        -----
        currently, the color of the vector does not support the matplotlib's color code due to the implementation

        See Also
        --------
        add_vectors : add multiple vectors to be displayed
        """
        vector_plotting.add_vector(self._ax, vector, position, length, color)

    def add_vectors(self, vectors: list[Vector], positions: list[Point] = None, length: float = 0.025, color: str = 'k') -> None:
        """
        add multiple vectors to be displayed

        Parameters
        ----------
        vectors : list[~.entities.vector.Vector]
            vectors to be added

        positions : list[~.entities.point.Point], optional
            list of positions of each vector. By default on the origin

        length : float, optional
            the length of the displayed vectors. 0.025 by default

        color : str, optional
            the color of the plotted vector. 'k' black by default. Currently only supports 'k' (black), 'r' (red), 'g' (green) and 'b' (blue)

        Raises
        ------
        IndexError
            if the lengths of the vector and position list do not match

        Notes
        -----
        currently, the color of the vector does not support the matplotlib's color code due to the implementation

        See Also
        --------
        add_vector : add a vector to be displayed
        """
        if positions is None:
            positions: list[Point] = [Point(0.0, 0.0, 0.0)]*len(vectors)

        if len(vectors) != len(positions):
            raise IndexError(
                'the lengths of the vectors and positions do not match')

        vector_plotting.add_vectors(
            self._ax, vectors, positions, length, color)

    # ==========
    # AXES
    # ==========
    def add_axes(self, axes: Axes, position: Point = Point(0.0, 0.0, 0.0), length: float = 0.025) -> None:
        """
        adds axes to be displayed

        Parameters
        ----------
        axes : ~.entities.axes.Axes
            the axes to be displayed

        position : ~.entities.point.Point, optional
            the position of the axes. By default on the origin

        length : float, optional
            the length of the displayed axes. 0.025 by default

        See Also
        --------
        add_multiple_axes : adds multiple axes to be displayed
        """
        axes_plotting.add_axes(self._ax, axes, position, length)

    def add_multiple_axes(self, axes_list: list[Axes], positions: list[Point] = None, length: float = 0.025) -> None:
        """
        adds multiple axes to be displayed

        Parameters
        ----------
        axes_list : list[~.entities.axes.Axes]
            the list of axes to be displayed

        positions : list[~.entities.point.Point], optional
            the positions of the axes. By default on the origin

        length : float, optional
            the length of the plotted axes. 0.025 by default

        Raises
        ------
        IndexError
            if the lengths of the axes list and positions do not match

        See Also
        --------
        add_axes : adds axes to be displayed
        """
        if positions is None:
            positions: list[Point] = [Point(0.0, 0.0, 0.0)]*len(axes_list)

        if len(axes_list) != len(positions):
            raise IndexError(
                'the lengths of the axes and position list do not match')

        axes_plotting.add_multiple_axes(self._ax, axes_list, positions, length)

    # ==========
    # LINES
    # ==========
    def add_line(self, line: Line, line_range: tuple[float] = (-2.0, 2.0), style: str = '-', color: str = 'k') -> None:
        """
        adds a line to be displayed

        Parameters
        ----------
        line : ~.entities.line.Line
            the line to be displayed

        line_range : tuple[float], optional
             the range of the line to be plotted. From -2.0 to 2.0 by default

        style : str, optional
            the style of the line. Follows the matplotlib's style code. '-' by default

        color : str, optional
            the color of the displayed line. Follows the matplotlib's color code. 'k' (black) by default

        See Also
        --------
        add_lines : adds multiple lines to be displayed
        """
        line_plotting.add_line(self._ax, line, line_range, style, color)

    def add_lines(self, lines: list[Line], line_range: tuple[float] = (-2.0, 2.0), style: str = '-', color: str = 'k') -> None:
        """
        adds multiple lines to be displayed

        Parameters
        ----------
        lines : list[~.entities.line.Line]
            the list of lines to be displayed

        line_range : tuple[float], optional
             the range of the lines to be plotted. From -2.0 to 2.0 by default

        style : str, optional
            the style of the lines. Follows the matplotlib's style code. '-' by default

        color : str, optional
            the color of the displayed lines. Follows the matplotlib's color code. 'k' (black) by default

        See Also
        --------
        add_line : adds line to be displayed
        """
        line_plotting.add_lines(self._ax, lines, line_range, style, color)

    # ==========
    # PLANES
    # ==========
    def add_plane(self, plane: Plane, center: Point = Point(0.0, 0.0, 0.0), size: float = 0.2, alpha: float = 0.5) -> None:
        """
        adds plane to be displayed

        Parameters
        ----------
        plane : ~.entities.plane.Plane
            the plane to be displayed

        center : ~.entities.point.Point, optional
            the center point of the plane. By default on the origin

        size : float, optional
            the size of the plane. 0.2 by default

        alpha : float, optional
            the opacity value. 0.5 by default

        See Also
        --------
        add_planes : adds multiple planes to be displayed
        """
        plane_plotting.add_plane(self._ax, plane, center, size, alpha)

    def add_planes(self, planes: list[Plane], centers: list[Point] = None, size: float = 0.2, alpha: float = 0.5) -> None:
        """
        adds multiple planes to be displayed

        Parameters
        ----------
        planes : list[~.entities.plane.Plane]
            the list of planes to be displayed

        centers : list[~.entities.point.Point], optional
            the list of the center of each plane. By default on the origin

        size : float, optional
            the sizes of the planes. 0.2 by default

        alpha : float, optional
            the opacity value. 0.5 by default

        Raises
        ------
        IndexError
            if the lengths of the plane and center list do not match

        See Also
        --------
        add_plane : adds plane to be displayed
        """
        if centers is None:
            centers: list[Point] = [Point(0.0, 0.0, 0.0)]*len(planes)

        if len(planes) != len(centers):
            raise IndexError(
                'the lengths of the plane and center list do not match')

        plane_plotting.add_planes(self._ax, planes, centers, size, alpha)
