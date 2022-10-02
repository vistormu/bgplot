import bgplot as bgp
from bgplot.entities import Point, Vector

graphics: bgp.Graphics = bgp.Graphics()

# Vector plotting
vector_1: Vector = Vector(1.0, 0.0, 0.0)
vector_2: Vector = Vector(0.0, 1.0, 0.0)
vector_3: Vector = Vector(0.0, 0.0, 1.0)

graphics.add_vector(vector_1, length=0.1)
graphics.add_vector(vector_2, length=0.2, color='r')
graphics.add_vector(vector_3, length=0.05, color='b')

graphics.set_title('vector')
graphics.show()

# Multiple vectors plotting
graphics.add_vectors([vector_1, vector_2, vector_3], [Point(0.0, 0.0, 0.0), Point(
    1.0, 0.0, 0.0), Point(0.0, 0.0, 1.0)], length=0.1, color='b')

graphics.set_title('vectors')
graphics.show()
