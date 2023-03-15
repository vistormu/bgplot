# bgplot

![alt text](/bgplot/assets/bgplot_logo.png)

Basic Geometry Plotter (bgplot) is a simple python library used for fast and quick geometric graphics representation. It is built on top of matplotlib, so it also offers all its capabilities,

## Installation

Follow the next steps for installing the simulation on your device.

**Requierements:**
- Ubuntu
- Python 3.10.0 or higher

### Install miniconda (highly-recommended)
It is highly recommended to install all the dependencies on a new virtual environment. For more information check the conda documentation for [installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and [environment management](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). For creating the environment use the following commands on the terminal.

```bash
conda create -n bgplot python==3.10.8
conda activate bgplot
```

### Install from pip
BGPlot is available as a pip package. For installing it just use:

```
pip install bgplot
```

### Install from source
Firstly, clone the repository in your system.
```bash
git clone https://github.com/vistormu/bgplot.git
```

Then, enter the directory and install the required dependencies
```bash
cd bgplot
pip install -r requirements.txt
```

## Documentation
Visit [the official documentation](https://bgplot.readthedocs.io/en/latest/)

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
plane: Plane = Plane.from_normal_vector_and_point(Vector(0.0, 0.0, 1.0), Point(0.0, 0.0, 0.0))
axes: Axes = Axes(Vector(1.0, 0.0, 0.0),
                  Vector(0.0, 1.0, 0.0),
                  Vector(0.0, 0.0, 1.0))
intersection_point: Point = bgp.ops.get_intersection_of_line_and_plane(line, plane)

# Representation
graphics.add_point(point)
graphics.add_vector(vector, position=point, color=bgp.Colors.pink)
graphics.add_line(line, style='--', line_range=(0.0, 1.0),
                  color=bgp.Colors.gray, width=0.7)
graphics.add_plane(plane, center=intersection_point, alpha=0.3)
graphics.add_axes(axes)
graphics.add_point(intersection_point, color=bgp.Colors.red)

graphics.set_title('Visual representation')
graphics.show()

```
![alt text](/bgplot/assets/bgplot_figure.png)
