import bgplot as bgp
from bgplot.entities import Point, Line, Axes, Vector

from bgplot.features.graphics.core.colors import Colors

graphics: bgp.Graphics = bgp.Graphics()

point_1: Point = Point(1.0, 1.0, 1.0)
point_2: Point = Point(0.0, 0.0, 0.0)
line: Line = Line.from_two_points(point_1, point_2)

color_list: list[str] = [Colors.black, Colors.blue, Colors.gray, Colors.green,
                         Colors.pink, Colors.purple, Colors.red, Colors.white, Colors.yellow]

# Points
# for color in color_list:
#     graphics.add_point(point_1, color=color)
#     graphics.set_title(f'{color}')
#     graphics.update(1)

# # Lines
# for color in color_list:
#     graphics.add_points([point_1, point_2], color=color)
#     graphics.add_line(line, color=color)
#     graphics.set_title(f'{color}')
#     graphics.update(1)

# Vectors
for color in color_list:
    graphics.add_points([point_1, point_2], color=color)
    graphics.add_vector(Vector(*point_1), position=point_2)
    graphics.set_title(f'{color}')
    graphics.update(1)
