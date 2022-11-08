import numpy as np
from typing import NamedTuple, Self


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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.u}, {self.v}, {self.w})'

    def __mul__(self, scalar) -> Self:
        return Vector(self.u*scalar, self.v*scalar, self.w * scalar)

    def __rmul__(self, scalar) -> Self:
        return Vector(self.u*scalar, self.v*scalar, self.w * scalar)

    def __add__(self, other: Self) -> Self:
        return Vector(self.u+other.u, self.v+other.v, self.w+other.w)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.u-other.u, self.v-other.v, self.w-other.w)

    def __truediv__(self, scalar) -> Self:
        return Vector(self.u/scalar, self.v/scalar, self.w/scalar)

    def normalize(self) -> Self:
        """
        normalizes the vector so its magnitude is unitary

        Returns
        -------
        out : ~.entities.vector.Vector
            the normalized instance of the vector
        """
        length: float = np.linalg.norm(self).astype(float)
        u: float = self.u / length
        v: float = self.v / length
        w: float = self.w / length

        return Vector(u, v, w)
