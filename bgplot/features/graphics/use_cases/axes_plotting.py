from matplotlib.axes import Axes as mplAxes

from ....entities import Axes, Point


def add_axes(figure: mplAxes, axes: Axes, position: Point, length: float) -> None:
    figure.quiver(position.x, position.y, position.z,
                  axes.x.u, axes.x.v, axes.x.w,
                  length=length,
                  colors=(1.0, 0.0, 0.0))

    figure.quiver(position.x, position.y, position.z,
                  axes.y.u, axes.y.v, axes.y.w,
                  length=length,
                  colors=(0.0, 1.0, 0.0))

    figure.quiver(position.x, position.y, position.z,
                  axes.z.u, axes.z.v, axes.z.w,
                  length=length,
                  colors=(0.0, 0.0, 1.0))


def add_multiple_axes(figure: mplAxes, axes_list: list[Axes], positions: list[Point], length: float) -> None:
    x: list[float] = [point.x for point in positions]
    y: list[float] = [point.y for point in positions]
    z: list[float] = [point.z for point in positions]
    u_x: list[float] = [axes.x.u for axes in axes_list]
    v_x: list[float] = [axes.x.v for axes in axes_list]
    w_x: list[float] = [axes.x.w for axes in axes_list]
    u_y: list[float] = [axes.y.u for axes in axes_list]
    v_y: list[float] = [axes.y.v for axes in axes_list]
    w_y: list[float] = [axes.y.w for axes in axes_list]
    u_z: list[float] = [axes.z.u for axes in axes_list]
    v_z: list[float] = [axes.z.v for axes in axes_list]
    w_z: list[float] = [axes.z.w for axes in axes_list]

    figure.quiver(x, y, z,
                  u_x, v_x, w_x,
                  length=length,
                  colors=(1.0, 0.0, 0.0))

    figure.quiver(x, y, z,
                  u_y, v_y, w_y,
                  length=length,
                  colors=(0.0, 1.0, 0.0))

    figure.quiver(x, y, z,
                  u_z, v_z, w_z,
                  length=length,
                  colors=(0.0, 0.0, 1.0))
