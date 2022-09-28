import bgplot as bgp
from bgplot import Line, Point, Plane, Vector

graphics: bgp.Graphics = bgp.Graphics()
graphics.set_limits((0.0, 1.0), (0.0, 1.0), (0.0, 1.0))

p_1 = Point(0.0, 0.0, 0.0)
p_2 = Point(1.0, 1.0, 1.0)
n = Vector(0.0, 0.0, 1.0)
line = Line.from_two_points(p_1, p_2)
plane = Plane.from_normal_vector(n, p_1)

proj_line = bgp.project_line_on_plane(line, plane)

graphics.add_plane(plane)
graphics.add_line(line)
graphics.add_line(proj_line)
graphics.add_points([p_1, p_2])

graphics.show()
graphics.close()
