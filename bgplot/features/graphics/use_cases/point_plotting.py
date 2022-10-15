from matplotlib.axes import Axes as mplAxes

from ....entities import Point, Axes, OrientedPoint
from ..core.colors import Colors

# TMP


def _get_color(value: str) -> tuple[float, float, float, float]:
    stripped_code = value.lstrip('#')
    rgb_value = tuple(int(stripped_code[i:i+2], 16) for i in (0, 2, 4))
    r: float = rgb_value[0]/255.0
    g: float = rgb_value[1]/255.0
    b: float = rgb_value[2]/255.0

    return (r, g, b)


def add_point(figure: mplAxes, point: Point, color: str) -> None:
    figure.scatter(*point, c=color)


def add_points(figure: mplAxes, points: list[Point], style: str, color: str, linewidth: float) -> None:
    x: list[float] = [point.x for point in points]
    y: list[float] = [point.y for point in points]
    z: list[float] = [point.z for point in points]

    figure.plot(x, y, z, style, c=color, lw=linewidth)


def add_oriented_point(figure: mplAxes, oriented_point: OrientedPoint, length: float, color: str) -> None:
    figure.quiver(*oriented_point.position,
                  *oriented_point.axes.x,
                  length=length,
                  colors=_get_color(Colors.red))

    figure.quiver(*oriented_point.position,
                  *oriented_point.axes.y,
                  length=length,
                  colors=_get_color(Colors.green))

    figure.quiver(*oriented_point.position,
                  *oriented_point.axes.z,
                  length=length,
                  colors=_get_color(Colors.blue))

    figure.scatter(*oriented_point.position, c=color)


def add_oriented_points(figure: mplAxes, oriented_points: list[OrientedPoint], style: str, length: float, color: str, linewidth: float) -> None:
    x: list[float] = [
        oriented_point.position.x for oriented_point in oriented_points]
    y: list[float] = [
        oriented_point.position.y for oriented_point in oriented_points]
    z: list[float] = [
        oriented_point.position.z for oriented_point in oriented_points]
    u_x: list[float] = [
        oriented_point.axes.x.u for oriented_point in oriented_points]
    v_x: list[float] = [
        oriented_point.axes.x.v for oriented_point in oriented_points]
    w_x: list[float] = [
        oriented_point.axes.x.w for oriented_point in oriented_points]
    u_y: list[float] = [
        oriented_point.axes.y.u for oriented_point in oriented_points]
    v_y: list[float] = [
        oriented_point.axes.y.v for oriented_point in oriented_points]
    w_y: list[float] = [
        oriented_point.axes.y.w for oriented_point in oriented_points]
    u_z: list[float] = [
        oriented_point.axes.z.u for oriented_point in oriented_points]
    v_z: list[float] = [
        oriented_point.axes.z.v for oriented_point in oriented_points]
    w_z: list[float] = [
        oriented_point.axes.z.w for oriented_point in oriented_points]

    figure.quiver(x, y, z,
                  u_x, v_x, w_x,
                  length=length,
                  colors=_get_color(Colors.red))

    figure.quiver(x, y, z,
                  u_y, v_y, w_y,
                  length=length,
                  colors=_get_color(Colors.green))

    figure.quiver(x, y, z,
                  u_z, v_z, w_z,
                  length=length,
                  colors=_get_color(Colors.blue))

    figure.plot(x, y, z, style, c=color, lw=linewidth)
