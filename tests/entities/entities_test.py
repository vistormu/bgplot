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
htm: np.ndarray = np.array([[*axes.x, 0.0],
                            [*axes.y, 0.0],
                            [*axes.z, 0.0],
                            [*point, 1.0]]).T

oriented_point: OrientedPoint = OrientedPoint.from_htm(htm)

Logger.info(htm)
Logger.info(oriented_point)
Logger.info('%%%%%%')

htm: np.ndarray = oriented_point.to_htm()

Logger.info(htm)
Logger.info(oriented_point)
Logger.info('%%%%%%')

# Operations
point_1: Point = Point(1.0, 0.0, 0.0)
point_2: Point = Point(0.0, 1.0, 0.0)

Logger.info('add: ', point_1+point_2)
Logger.info('sub: ', point_1-point_2)
Logger.info('mul: ', point_1*0.2)
Logger.info('mul: ', 0.1*point_1)
Logger.info('div: ', point_1/0.1)
Logger.info('%%%%%%')

vector_1: Vector = Vector(1.0, 0.0, 0.0)
vector_2: Vector = Vector(0.0, 1.0, 0.0)

Logger.info('add: ', vector_1+vector_2)
Logger.info('sub: ', vector_1-vector_2)
Logger.info('mul: ', vector_1*0.2)
Logger.info('mul: ', 0.1*vector_1)
Logger.info('div: ', vector_1/0.1)
Logger.info('%%%%%%')
