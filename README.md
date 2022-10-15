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
graphics: bgp.Gaphics = bgp.Graphics()

# Personalize the graphic representation
graphics.set_limits(xlim=(-2.0, 2.0),
                    ylim=(-2.0, 2.0),
                    zlim=(0.0, 1.0))
graphics.set_view(-15.0, 45.0)
graphics.disable('ticks', 'axes', 'walls')
graphics.set_background_color(bgp.Colors.white)

# Entities
point_1: Point = Point(1.0, 1.0, 1.0)
point_2: Point = Point()

WIP
```

## Documentation
