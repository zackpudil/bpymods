from ..types import GLSLVector, GLSLMatrix
from ..utils import is_matrix, is_vector


def gen_type(vs, r):
    if any([is_matrix(v) for v in vs]):
        return GLSLMatrix(r)
    elif any([is_vector(v) for v in vs]):
        return GLSLVector(r)
    else:
        return r
