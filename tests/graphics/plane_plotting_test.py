import numpy as np
import bgplot as bgp
from bgplot.entities import Point, Vector, Plane, Line

graphics: bgp.Graphics = bgp.Graphics()

# simple planes
point_1: Point = Point(1.0, 0.0, 0.0)
point_2: Point = Point(0.0, 1.0, 0.0)
point_3: Point = Point(0.0, 0.0, 1.0)

vector_1: Vector = Vector(*(point_1-point_2)).normalize()
vector_2: Vector = Vector(*(point_1-point_3)).normalize()
normal_vector = Vector(*np.cross(vector_1, vector_2)).normalize()

line: Line = Line.from_two_points(point_2, point_3)

plane_1: Plane = Plane.from_line_and_point(line, point_1)
plane_2: Plane = Plane.from_normal_vector_and_point(normal_vector, point_1)
plane_3: Plane = Plane.from_three_points(point_1, point_2, point_3)
plane_4: Plane = Plane.from_two_vectors_and_point(vector_1, vector_2, point_1)

graphics.add_plane(plane_1)
graphics.add_plane(plane_2)
graphics.add_plane(plane_3)
graphics.add_plane(plane_4)

graphics.set_title('plane')
graphics.show()

# multiple planes
graphics.add_planes([plane_1, plane_2, plane_3, plane_4], [point_1]*4)

graphics.set_title('planes')
graphics.show()
