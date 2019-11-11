from ..types import GLSLVector
from ..utils import is_vector


def vec2(x, y=None):
    if y is None:
        return GLSLVector([x, x])

    return GLSLVector([x, y])


def vec3(x, y=None, z=None):
    if x is not None and z is not None:
        return GLSLVector([x, y, z])
    elif y is not None:
        if is_vector(x):
            return GLSLVector(x.coordinates + [y])
        elif is_vector(y):
            return GLSLVector([x] + y.coordinates)

    if y is None and z is None:
        return GLSLVector([x, x, x])


def vec4(x, y=None, z=None, w=None):
    if y is not None and z is not None and w is not None:
        return GLSLVector([x, y, z, w])

    if y is not None and z is not None:
        if is_vector(x):
            return GLSLVector(x.coordinates + [y, z])
        elif is_vector(y):
            return GLSLVector([x] + y.coordinates + [z])
        elif is_vector(z):
            return GLSLVector([x, y] + z.coordinates)

    if y is not None:
        if is_vector(x) and is_vector(y):
            return GLSLVector(x.coordinates + y.coordinates)
        elif is_vector(x):
            return GLSLVector(x.coordinates + [y])
        elif is_vector(y):
            return GLSLVector([x] + y.coordinates)

    if y is None and z is None and w is None:
        return GLSLVector([x, x, x, x])
