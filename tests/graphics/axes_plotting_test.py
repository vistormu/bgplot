import bgplot as bgp
from bgplot.entities import Point, Axes, Vector

graphics: bgp.Graphics = bgp.Graphics()

# Simples axes
axes_1: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 0.0),
                    Vector(0.0, 0.0, 1.0))

axes_2: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 1.0),
                    Vector(0.0, 0.0, 1.0))

axes_3: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 0.0),
                    Vector(1.0, 0.0, -1.0))

graphics.add_axes(axes_1)
graphics.add_axes(axes_2)
graphics.add_axes(axes_3)

graphics.set_title('axes')
graphics.show()

# Multiple axes
graphics.add_multiple_axes([axes_1, axes_2, axes_3], [Point(
    0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(1.0, 1.0, 0.0)], length=0.1)

graphics.set_title('multiple axes')
graphics.show()
