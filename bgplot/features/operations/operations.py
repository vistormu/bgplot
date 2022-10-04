import numpy as np

from ...entities import Vector, Line, Point, Plane
from .use_cases import projections, angles, intersections, distances


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
    return projections.project_vector_on_plane(vector, plane)


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
    return projections.project_line_on_plane(line, plane)


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
    Note that depending on the direction of the normal vector, the returned angle could be angle or pi+angle

    """
    return angles.get_angle_of_two_vectors(vector_1, vector_2, normal_vector, degrees)


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
    return intersections.get_intersection_of_line_and_plane(line, plane)


def distance_between_two_points(point_1: Point, point_2: Point) -> float:
    """
    returns the distance between tow points in space

    Parameters
    ----------
    point_1 : ~.entities.point.Point
        the first point

    point_2 : ~.entities.point.Point
        the second point

    Returns
    -------
    out : float
        the distance between the two points
    """
    return distances.distance_between_two_points(point_1, point_2)
