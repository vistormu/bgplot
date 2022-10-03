import numpy as np
from typing import NamedTuple


class Vector(NamedTuple):
    """
    a named tuple that contains the information of a 3D free vector in space

    Attributes
    ----------
    u : float
        the value of the first element on the u-v-w axes

    v : float
        the value of the second element on the u-v-w axes

    w : float
        the value of the third element on the u-v-w axes

    Notes
    -----
    supports addition and subtraction with other Vector class instances.
    supports scalar multiplication
    """
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
        """
        normalizes the vector so its magnitude is unitary

        Returns
        -------
        out : ~.entities.vector.Vector
            the normalized instance of the vector
        """
        length: float = np.linalg.norm(self)
        u: float = self.u / length
        v: float = self.v / length
        w: float = self.w / length

        return Vector(u, v, w)
