import numpy as np

from ..entities import Vector, Line, Point, Plane


def project_vector_on_plane(vector: Vector, plane: Plane) -> Vector:
    """
    returns the projected vector on a given plane

    Parameters
    ----------
    vector : ~.entities.vector.Vector
        the desired vector to project

    plane : ~.entities.plane.Plane
        the plane to project the vector

    Returns
    -------
    out : ~.entities.vector.Vector
        the projection of the vector on the plane

    See Also
    --------
    project_line_on_plane : returns the projected line on a given plane
    """
    u: np.ndarray = np.array(vector)
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    v: np.ndarray = u - np.dot(u, n)/np.power(np.linalg.norm(n), 2)*n

    v_vector: Vector = Vector(*v)

    return v_vector


def project_line_on_plane(line: Line, plane: Plane) -> Line:
    """
    returns the projected line on a given plane

    Parameters
    ----------
    line : ~.entities.line.Line
        the desired line to project

    plane : ~.entities.plane.Plane
        the plane to project the line

    Returns
    -------
    out : ~.entities.line.Line
        the projection of the line on the plane

    See Also
    --------
    project_vector_on_plane : returns the projected vector on a given plane
    """
    u: np.ndarray = np.array([line.u, line.v, line.w])
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    v: np.ndarray = u - np.dot(u, n)/np.power(np.linalg.norm(n), 2)*n

    point: Point = get_intersection_of_line_and_plane(line, plane)
    projected_line: Line = Line.from_vector_and_point(Vector(*v), point)

    return projected_line


def get_angle_of_two_vectors(vector_1: Vector, vector_2: Vector, normal_vector: Vector, degrees: bool = False) -> float:
    """
    returns the angle of two vectors on the plane specified by a normal vector

    Parameters
    ----------
    vector_1 : ~.entities.vector.Vector
        first vector

    vector_2 : ~.entities.vector.Vector
        second vector vector

    normal_vector : ~.entities.vector.Vector
        the normal vector of the plane

    degrees : bool, optional
        specifies if the return value should be given in degrees. False by default

    Returns
    --------
    out : float
        the angle of the two vectors on the given plane

    Notes
    -----
    Note that depending on the direction of the normal vector, the returned angle could be angle or 2*pi-angle

    """
    v1: np.ndarray = np.array(vector_1.normalize())
    v2: np.ndarray = np.array(vector_2.normalize())
    n: np.ndarray = np.array(normal_vector.normalize())

    angle: float = np.arctan2(np.dot(np.cross(v2, v1), n), np.dot(v1, v2))

    if angle < 0.0:
        angle += 2.0*np.pi

    return angle if not degrees else angle*180/np.pi


def get_intersection_of_line_and_plane(line: Line, plane: Plane) -> Point:
    """
    returns the point of intersection of a line and a plane

    Parameters
    ----------
    line : ~.entities.line.Line
        the line that intersects the plane

    plane: ~.entities.plane.Plane
        the intersected plane by the line

    Returns
    -------
    out : ~.entities.point.Point
        the point of intersection of the line and the plane

    Raises
    ------
    ValueError
        if the plane and the line are parallel to each other

    """
    v: np.ndarray = np.array([line.u, line.v, line.w])
    n: np.ndarray = np.array([plane.a, plane.b, plane.c])
    line_point: np.ndarray = np.array([line.x, line.y, line.z])

    dot_product: float = np.dot(n, v)

    if abs(dot_product) < 0.01:
        raise ValueError('the plane and the line are parallel to each other')

    t: float = -(plane.d+np.dot(n, line_point))/dot_product

    intersection_point: Point = Point(*(line_point + v*t))

    return intersection_point
