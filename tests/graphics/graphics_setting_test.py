import bgplot as bgp
from bgplot.entities import Point

graphics: bgp.Graphics = bgp.Graphics()
graphics.set_limits((0.0, 1.0), (0.0, 1.0), (0.0, 1.0))

# locked limits
point: Point = Point(0.0, 0.0, 0.0)

graphics.add_point(point, 'r')
graphics.show()

point: Point = Point(-1.0, 0.0, 0.0)
graphics.add_point(point)
graphics.show()
