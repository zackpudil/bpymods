from .glsl_type import GLSLType
from ..utils import reduce_exec_to_comps, is_matrix


class GLSLVector(GLSLType):
    coordinates = []

    names = {
        'x': 0,
        'y': 1,
        'z': 2,
        'w': 3,
        'r': 0,
        'g': 1,
        'b': 2,
        'a': 3
    }

    @property
    def columns(self):
        return [self.transpose()]

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        params = [str(c) for c in self.coordinates]
        return "vec{0}({1})".format(str(len(self.coordinates)), ','.join(params))

    def __getattr__(self, attr):
        nv = [self.coordinates[self.names.get(c)] for c in list(attr)]

        return nv.pop() if len(nv) == 1 else GLSLVector(nv)

    def __setattr__(self, attr, value):
        if attr == "coordinates":
            super().__setattr__(attr, value)
            return

        s = list(attr)
        for i in range(0, len(s)):
            self.coordinates[self.names.get(s[i])] = value if len(s) == 1 else value.coordinates[i]

    def transpose(self):
        return GLSLVector(self.coordinates)

    def add(self, v):
        return GLSLVector(reduce_exec_to_comps((self, v), lambda a, b: a + b))

    def sub(self, v):
        return GLSLVector(reduce_exec_to_comps((self, v), lambda a, b: a - b))

    def mul(self, v):
        if is_matrix(v):
            return NotImplemented
        return GLSLVector(reduce_exec_to_comps((self, v), lambda a, b: a * b))

    def rmul(self, v):
        if is_matrix(v):
            return NotImplemented
        return self.mul(v)

    def truediv(self, v):
        return GLSLVector(reduce_exec_to_comps((self, v), lambda a, b: a / b))

    def neg(self):
        return GLSLVector([-c for c in self.coordinates])

    def abs(self):
        return GLSLVector([abs(c) for c in self.coordinates])
