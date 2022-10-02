from matplotlib.axes import Axes as mplAxes

from ....entities import Vector, Point


def add_vector(figure: mplAxes, vector: Vector, position: Point, length: float, color: str) -> None:
    color_dict: dict = {'r': (1.0, 0.0, 0.0),
                        'g': (0.0, 1.0, 0.0),
                        'b': (0.0, 0.0, 1.0),
                        'k': (0.0, 0.0, 0.0)}

    figure.quiver(position.x, position.y, position.z,
                  vector.u, vector.v, vector.w,
                  length=length,
                  colors=color_dict[color])


def add_vectors(figure: mplAxes, vectors: list[Vector], positions: list[Point], length: float, color: str) -> None:
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

    figure.quiver(x, y, z,
                  u, v, w,
                  length=length,
                  colors=color_dict[color])
