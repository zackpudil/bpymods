from math import sqrt
from functools import reduce
from itertools import chain

from .glsl_type import GLSLType
from .glsl_vector import GLSLVector
from ..utils import reduce_exec_to_comps, is_matrix, is_vector, is_glsl_type

class GLSLMatrix(GLSLType):

    cols = []

    @property
    def coords(self):
        return list(reduce(lambda x, y: chain(x, y.coords), self.cols, []))

    def __init__(self, elements):
        row_len = (int)(sqrt(len(elements)))
        self.cols = [GLSLVector(elements[j:(j+row_len)]) for j in range(0, len(elements), row_len)]

    def __str__(self):
        row_str = [','.join([str(x) for x in v.coords]) for v in self.transpose().cols]
        return 'mat{0}(\n  {1}\n)'.format(str(len(self.cols)), '\n  '.join(row_str))

    def transpose(self):
        vs = [GLSLVector([v.coords[i] for v in self.cols]) for i in range(0, len(self.cols))]

        return GLSLMatrix(list(reduce(lambda x, y: chain(x, y.coords), vs, [])))

    def add(self, m):
        return GLSLMatrix(reduce_exec_to_comps((self, m), lambda x, y: x + y))

    def sub(self, m):
        return self.add(-m)

    def neg(self):
        return GLSLMatrix(reduce_exec_to_comps((self,), lambda x: -x))

    def mul(self, m):
        if is_glsl_type(m):
            els = [sum((x*y).coords) for x in self.transpose().cols for y in m.cols]

            if is_matrix(m):
                return GLSLMatrix(els).transpose()
            else:
                return GLSLVector(els)
        else:
            return GLSLMatrix(reduce_exec_to_comps((self, m), lambda x, y: x*y))

    def rmul(self, m):
        if is_glsl_type(m):
            return self.transpose().mul(m)
        else:
            return self.mul(m)