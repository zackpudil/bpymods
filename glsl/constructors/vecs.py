from functools import reduce

from ..types import GLSLVector
from ..utils import is_vector


def vec2(*args):
    return __vec__(args, 2)


def vec3(*args):
    return __vec__(args, 3)


def vec4(*args):
    return __vec__(args, 4)


def __vec__(elements, vec_len):
    if len(elements) == vec_len:
        return GLSLVector(list(elements))
    elif len(elements) == 1:
        if is_vector(elements[0]):
            return GLSLVector(elements[0].coordinates[:])
        else:
            return GLSLVector([elements[0]] * vec_len)
    else:
        coordinates = [x.coordinates if is_vector(x) else [x] for x in elements]
        return GLSLVector(list(reduce(lambda x, y: x + y, coordinates, [])))
