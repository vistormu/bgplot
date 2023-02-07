import bgplot as bgp
from bgplot.entities import Point, Axes, Vector, OrientedPoint

graphics: bgp.Graphics = bgp.Graphics()

graphics.set_limits((0.0, 1.0), (0.0, 1.0), (0.0, 1.0))
graphics.set_view(20.0, 20.0)
graphics.disable('grid', 'axes', 'walls', 'ticks')
graphics.set_background_color(bgp.Colors.white, part='floor')

# Simple point plotting
point_1: Point = Point(0.0, 0.0, 0.0)
point_2: Point = Point(1.0, 1.0, 0.0)
point_3: Point = Point(1.0, 1.0, 1.0)

graphics.add_point(point_1, color=bgp.Colors.red)
graphics.add_point(point_2, color=bgp.Colors.green)
graphics.add_point(point_3, color=bgp.Colors.blue)

graphics.set_title('point')
graphics.show()

# Multiple points plotting
graphics.add_points([point_1, point_2, point_3], style='.-')

graphics.set_title('points')
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

oriented_point_1: OrientedPoint = OrientedPoint(point_1, axes_1)
oriented_point_2: OrientedPoint = OrientedPoint(point_2, axes_2)
oriented_point_3: OrientedPoint = OrientedPoint(point_3, axes_3)

graphics.add_oriented_point(oriented_point_1, color=bgp.Colors.red)
graphics.add_oriented_point(oriented_point_2, color=bgp.Colors.green)
graphics.add_oriented_point(oriented_point_3, color=bgp.Colors.blue)

graphics.set_title('oriented point')
graphics.show()

# Multiple oriented points

graphics.set_title('oriented points')
graphics.add_oriented_points(
    [oriented_point_1, oriented_point_2, oriented_point_3], style='.-', width=0.2)
graphics.set_background_color(bgp.Colors.white)
graphics.show()
