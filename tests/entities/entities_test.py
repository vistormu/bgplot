import numpy as np

from bgplot import Logger
from bgplot.entities import *

# Repr
point: Point = Point(1.0, 0.0, -1.0)
vector: Vector = Vector(0.0, -2.0, 3.0)
axes: Axes = Axes(Vector(1.0, 0.0, 0.0),
                  Vector(0.0, 1.0, 0.0),
                  Vector(0.0, 0.0, 1.0))
oriented_point: OrientedPoint = OrientedPoint(point, axes)

Logger.info(point)
Logger.info(vector)
Logger.info(axes)
Logger.info(oriented_point)
Logger.info('%%%%%%')

# HTM
htm: np.ndarray = np.array([[*axes.x, 0],
                            [*axes.y, 0],
                            [*axes.z, 0],
                            [*point, 1]]).T

oriented_point: OrientedPoint = OrientedPoint.from_htm(htm)

Logger.info(htm)
Logger.info(oriented_point)
Logger.info('%%%%%%')

htm: np.ndarray = oriented_point.to_htm()

Logger.info(htm)
Logger.info(oriented_point)
