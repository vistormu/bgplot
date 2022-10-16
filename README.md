# bgplot

![alt text](/bgplot/assets/bgplot_logo.png)

Basic Geometry Plotter (bgplot) is a simple python library used for fast and quick geometric graphics representation.

## Installation
```
pip install bgplot
```

## Basic Usage
```python
import bgplot as bgp
from bgplot.entities import Point, Vector, Line, Plane, Axes

# Create graphics object
graphics: bgp.Graphics = bgp.Graphics()

# Personalize the graphic representation
graphics.set_limits(xlim=(0.0, 1.2),
                    ylim=(0.0, 1.5),
                    zlim=(0.0, 1.0))
graphics.set_view(azimut=-50.0, elevation=20.0)
graphics.disable('ticks', 'axes', 'walls')
graphics.set_background_color(bgp.Colors.white)

# Entities
point: Point = Point(1.0, 1.0, 1.0)
vector: Vector = Vector(0.0, 0.0, -1.0)
line: Line = Line.from_vector_and_point(vector, point)
plane: Plane = Plane.from_normal_vector_and_point(Vector(0.0, 0.0, 1.0),
                                                  Point(0.0, 0.0, 0.0))
axes: Axes = Axes(Vector(1.0, 0.0, 0.0),
                  Vector(0.0, 1.0, 0.0),
                  Vector(0.0, 0.0, 1.0))
intersection_point: Point = bgp.ops.get_intersection_of_line_and_plane(line,
                                                                       plane)

# Representation
graphics.add_point(point)
graphics.add_vector(vector, position=point, color=bgp.Colors.pink)
graphics.add_line(line, style='--', line_range=(0.0, 1.0),
                  color=bgp.Colors.gray, linewidth=0.7)
graphics.add_plane(plane, center=intersection_point, alpha=0.3)
graphics.add_axes(axes)
graphics.add_point(intersection_point, color=bgp.Colors.red)

graphics.set_title('Visual representation')
graphics.show()

```
![alt text](/bgplot/assets/bgplot_figure.png)

## Documentation
