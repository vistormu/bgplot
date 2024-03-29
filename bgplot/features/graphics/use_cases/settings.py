from matplotlib.axes import Axes as mplAxes

# TMP
color_dict: dict = {'r': (1.0, 0.0, 0.0, 0.5),
                    'g': (0.0, 1.0, 0.0, 0.5),
                    'b': (0.0, 0.0, 1.0, 0.5),
                    'k': (0.0, 0.0, 0.0, 0.5),
                    'w': (1.0, 1.0, 1.0, 0.5)}


def _get_color(value: str) -> tuple[float, float, float, float]:
    if '#' in value:
        stripped_code = value.lstrip('#')
        rgb_value = tuple(int(stripped_code[i:i+2], 16) for i in (0, 2, 4))
        r: float = rgb_value[0]/255.0
        g: float = rgb_value[1]/255.0
        b: float = rgb_value[2]/255.0

        return (r, g, b, 0.5)
    else:
        return color_dict[value]


def disable_ticks(figure: mplAxes, input: tuple[str]) -> None:
    if 'ticks' in input:
        figure.tick_params(colors='white')
        # figure.set_xticks([])
        # figure.set_yticks([0], [''], color='white')
        # figure.set_zticks([0], [''], color='white')  # type: ignore
    if 'xticks' in input:
        figure.set_xticks([])
    if 'yticks' in input:
        figure.set_yticks([])
    if 'zticks' in input:
        figure.set_zticks([])  # type: ignore


def disable_axes(figure: mplAxes, input: tuple[str]) -> None:
    if 'axes' in input:
        figure.w_xaxis.line.set_visible(False)  # type: ignore
        figure.w_yaxis.line.set_visible(False)  # type: ignore
        figure.w_zaxis.line.set_visible(False)  # type: ignore
    if 'xaxis' in input:
        figure.w_xaxis.line.set_visible(False)  # type: ignore
    if 'yaxis' in input:
        figure.w_yaxis.line.set_visible(False)  # type: ignore
    if 'zaxis' in input:
        figure.w_zaxis.line.set_visible(False)  # type: ignore


def disable_grid(figure: mplAxes, input: tuple[str]) -> None:
    if 'grid' in input:
        figure.grid(False)


def disable_background(figure: mplAxes, input: tuple[str]) -> None:
    if 'background' in input:
        figure.xaxis.pane.fill = False  # type: ignore
        figure.yaxis.pane.fill = False  # type: ignore
        figure.zaxis.pane.fill = False  # type: ignore
        # TMP
        figure.xaxis.pane.set_edgecolor('w')  # type: ignore
        figure.yaxis.pane.set_edgecolor('w')  # type: ignore
        figure.zaxis.pane.set_edgecolor('w')  # type: ignore

    if 'walls' in input:
        figure.xaxis.pane.fill = False  # type: ignore
        figure.yaxis.pane.fill = False  # type: ignore

        figure.xaxis.pane.set_edgecolor('w')  # type: ignore
        figure.yaxis.pane.set_edgecolor('w')  # type: ignore

    if 'floor' in input:
        figure.zaxis.pane.fill = False  # type: ignore
        figure.zaxis.pane.set_edgecolor('w')  # type: ignore


def set_background_color(figure: mplAxes, color: str, part: str) -> None:
    if part == 'walls':
        figure.w_xaxis.set_pane_color(_get_color(color))  # type: ignore
        figure.w_yaxis.set_pane_color(_get_color(color))  # type: ignore
    elif part == 'floor':
        figure.w_zaxis.set_pane_color(_get_color(color))  # type: ignore
    else:
        figure.w_xaxis.set_pane_color(_get_color(color))  # type: ignore
        figure.w_yaxis.set_pane_color(_get_color(color))  # type: ignore
        figure.w_zaxis.set_pane_color(_get_color(color))  # type: ignore

    # TMP
    figure.xaxis.pane.set_edgecolor('w')  # type: ignore
    figure.yaxis.pane.set_edgecolor('w')  # type: ignore
    figure.zaxis.pane.set_edgecolor('w')  # type: ignore
