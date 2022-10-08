import bgplot as bgp
from bgplot.entities import Line, Point, Vector

graphics: bgp.Graphics = bgp.Graphics()

# simple line
line_1: Line = Line.from_two_points(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
line_2: Line = Line.from_vector_and_point(
    Vector(0.0, 1.0, 1.0), Point(0.0, 0.0, 0.0))

graphics.add_line(line_1)
graphics.add_line(line_2, line_range=(0.0, 1.0), style='--', color=bgp.Colors.gray)

graphics.set_title('line')
graphics.show()

# multiple lines
graphics.add_lines([line_1, line_2], color=bgp.Colors.red)

graphics.set_title('lines')
graphics.show()
