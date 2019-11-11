from itertools import chain
from ..types import GLSLMatrix


def mat2(*args):
    return __mat__(args)


def mat3(*args):
    return __mat__(args)


def mat4(*args):
    return __mat__(args)


def mat5(*args):
    return __mat__(args)


def __mat__(elements):
    if all([x is not None for x in elements]):
        return GLSLMatrix(list(elements))
    else:
        vs = filter(lambda x: x is not None, elements)
        return GLSLMatrix(list(chain(*[v.coordinates for v in vs])))
