from matplotlib.axes import Axes as mplAxes

from ....entities import Point, Axes


def add_point(figure: mplAxes, point: Point, color: str) -> None:
    figure.scatter(*point, c=color)


def add_points(figure: mplAxes, points: list[Point], style: str, color: str) -> None:
    x: list[float] = [point.x for point in points]
    y: list[float] = [point.y for point in points]
    z: list[float] = [point.z for point in points]

    figure.plot(x, y, z, style, c=color)


def add_oriented_point(figure: mplAxes, point: Point, axes: Axes, length: float, color: str) -> None:
    figure.scatter(*point, c=color)

    figure.quiver(*point, *axes.x,
                  length=length,
                  colors=(1.0, 0.0, 0.0))

    figure.quiver(*point, *axes.y,
                  length=length,
                  colors=(0.0, 1.0, 0.0))

    figure.quiver(*point, *axes.z,
                  length=length,
                  colors=(0.0, 0.0, 1.0))


def add_oriented_points(figure: mplAxes, points: list[Point], axes_list: list[Axes], style: str, length: float, color: str) -> None:
    x: list[float] = [point.x for point in points]
    y: list[float] = [point.y for point in points]
    z: list[float] = [point.z for point in points]
    # u: list

    # figure.plot(x, y, z, style, c=color)

    # figure.quiver(x, y, z,
    #               *axes.x,
    #               length=length,
    #               colors=(1.0, 0.0, 0.0))

    # figure.quiver(x, y, z,
    #               *axes.y,
    #               length=length,
    #               colors=(0.0, 1.0, 0.0))

    # figure.quiver(x, y, z,
    #               *axes.z,
    #               length=length,
    #               colors=(0.0, 0.0, 1.0))
