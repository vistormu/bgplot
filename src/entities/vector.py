import numpy as np
from typing import NamedTuple


class Vector(NamedTuple):
    u: float
    v: float
    w: float

    def normalize(self):
        length: float = np.linalg.norm(self)
        u: float = self.u / length
        v: float = self.v / length
        w: float = self.w / length

        return Vector(u, v, w)
