import bgplot as bgp
from bgplot.entities import Vector, Plane, Line, Point

graphics: bgp.Graphics = bgp.Graphics()

# project vector on plane
vector: Vector = Vector(1.0, 1.0, 1.0)
plane: Plane = Plane.from_normal_vector_and_point(
    Vector(0.0, 0.0, 1.0), Point(0.0, 0.0, 0.0))

vector_projected = bgp.op.project_vector_on_plane(vector, plane)

graphics.add_vector(vector)
graphics.add_vector(vector_projected)
graphics.add_plane(plane)

graphics.set_title('projection')
graphics.show()

# project line on plane
line: Line = Line.from_vector_and_point(vector, Point(0.0, 0.0, 0.0))
line_projected: Line = bgp.op.project_line_on_plane(line, plane)

graphics.add_lines([line, line_projected], style='--', line_range=(-0.2, 0.2))
graphics.add_plane(plane)

graphics.show()

# angle of two vectors
vector_1: Vector = Vector(1.0, 0.0, 0.0)
vector_2: Vector = Vector(0.0, 0.0, 1.0)

angle_1: float = bgp.op.get_angle_of_two_vectors(
    vector_1, vector_2, Vector(0.0, 1.0, 0.0), degrees=True)
angle_2: float = bgp.op.get_angle_of_two_vectors(
    vector_1, vector_2, Vector(0.0, -1.0, 0.0), degrees=True)

bgp.Logger.debug(angle_1, angle_2, sep=' ')

# Intersection of line and plane
intersection: Point = bgp.op.get_intersection_of_line_and_plane(line, plane)

graphics.add_point(intersection, color='r')
graphics.add_line(line, style='--', color='tab:gray', line_range=(-0.2, 0.2))
graphics.add_plane(plane)

graphics.set_title('intersection')
graphics.show()
