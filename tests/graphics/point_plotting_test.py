import bgplot as bgp
from bgplot.entities import Point, Axes, Vector

graphics: bgp.Graphics = bgp.Graphics()

# Simple point plotting
red_point: Point = Point(0.0, 0.0, 0.0)
green_point: Point = Point(1.0, 1.0, 0.0)
blue_point: Point = Point(1.0, 1.0, 1.0)

graphics.add_point(red_point, color='r')
graphics.add_point(green_point, color='g')
graphics.add_point(blue_point, color='b')

graphics.show()

# Multiple points plotting
graphics.add_points([red_point, green_point, blue_point], style='-o')

graphics.show()

# Oriented points
axes_1: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 0.0),
                    Vector(0.0, 0.0, 1.0))

axes_2: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 1.0),
                    Vector(0.0, 0.0, 1.0))

axes_3: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 0.0),
                    Vector(1.0, 0.0, -1.0))

# graphics.

# Multiple oriented points
