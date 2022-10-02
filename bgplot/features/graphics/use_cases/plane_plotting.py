import numpy as np
from matplotlib.axes import Axes as mplAxes

from ....entities import Plane, Point


def add_plane(figure: mplAxes, plane: Plane, center: Point, size: float, alpha: float) -> None:
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

    figure.plot_surface(plane_x, plane_y, plane_z, alpha=alpha)


def add_planes(figure: mplAxes, planes: list[Plane], centers: list[Point], size: float, alpha: float) -> None:
    for plane, center in zip(planes, centers):
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

        figure.plot_surface(plane_x, plane_y, plane_z, alpha=alpha)
