from itertools import chain
from ..types import GLSLMatrix


def mat2(a, b, c=None, d=None):
    return __mat__(locals().values())


def mat3(a, b, c, d=None, e=None, f=None, g=None, h=None, i=None):
    return __mat__(locals().values())


def mat4(a, b, c, d, e=None, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None, p=None):
    return __mat__(locals().values())


def __mat__(local_values):
    if all([x is not None for x in local_values]):
        return GLSLMatrix(list(local_values))
    else:
        vs = filter(lambda x: x is not None, local_values)
        return GLSLMatrix(list(chain(*[v.coordinates for v in vs])))
