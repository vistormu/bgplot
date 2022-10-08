import numpy as np
from matplotlib.axes import Axes as mplAxes

from ....entities import Line


def add_line(figure: mplAxes, line: Line, line_range: tuple[float], style: str, color: str, linewidth: float) -> None:
    t: np.ndarray = np.linspace(*line_range)
    x: np.ndarray = np.array(line.x + t*line.u)
    y: np.ndarray = np.array(line.y + t*line.v)
    z: np.ndarray = np.array(line.z + t*line.w)

    figure.plot(x, y, z, style, c=color, lw=linewidth)


def add_lines(figure: mplAxes, lines: list[Line], line_range: tuple[float], style: str, color: str, linewidth: float) -> None:
    for line in lines:
        t: np.ndarray = np.linspace(*line_range)
        x: np.ndarray = np.array(line.x + t*line.u)
        y: np.ndarray = np.array(line.y + t*line.v)
        z: np.ndarray = np.array(line.z + t*line.w)

        figure.plot(x, y, z, style, c=color, lw=linewidth)
