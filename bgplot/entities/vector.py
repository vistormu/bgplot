import numpy as np
from typing import NamedTuple


class Vector(NamedTuple):
    u: float
    v: float
    w: float

    def __mul__(self, scalar):
        return Vector(self.u*scalar, self.v*scalar, self.w * scalar)

    def __add__(self, other):
        return Vector(self.u+other.u, self.v+other.v, self.w+other.w)

    def __sub__(self, other):
        return Vector(self.u-other.u, self.v-other.v, self.w-other.w)

    def normalize(self):
        length: float = np.linalg.norm(self)
        u: float = self.u / length
        v: float = self.v / length
        w: float = self.w / length

        return Vector(u, v, w)
