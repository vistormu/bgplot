import numpy as np
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

# update
graphics.set_limits((0.0, 1.0), (0.0, 1.0), (0.0, 0.5))
graphics.set_view(20.0, 20.0)
graphics.disable('grid', 'axes', 'ticks', 'walls')
graphics.set_background_color(bgp.Colors.white, part='floor')


for _ in range(100):
    x: float = np.random.uniform(0.0, 1.0)

    graphics.add_point(Point(x, 0.0, 0.0), color=bgp.Colors.blue)

    graphics.update(10)
