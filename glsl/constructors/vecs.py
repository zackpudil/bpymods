from ..types import GLSLVector 
from ..utils import is_vector

def vec2(x, y=None):
    if y is None:
        return GLSLVector([x, x])

    return GLSLVector([x, y])

def vec3(x, y=None, z=None):
    if not x is None and not z is None:
        return GLSLVector([x, y, z])
    elif not y is None:
        if is_vector(x):
            return GLSLVector(x.coords + [y])
        elif is_vector(y):
            return GLSLVector([x] + y.coords)

    if y is None and z is None:
        return GLSLVector([x, x, x])

def vec4(x, y=None, z=None, w=None):
    if not y is None and not z is None and not w is None:
        return GLSLVector([x, y, z, w])

    if not y is None and not z is None:
        if is_vector(x):
            return GLSLVector(x.coords + [y, z])
        elif is_vector(y):
            return GLSLVector([x] + y.coords + [z])
        elif is_vector(z):
            return GLSLVector([x, y] + z.coords)

    if not y is None:
        if is_vector(x) and is_vector(y):
            return GLSLVector(x.coords + y.coords)
        elif is_vector(x):
            return GLSLVector(x.coords + [y])
        elif is_vector(y):
            return GLSLVector([x] + y.coords)

    if y is None and z is None and w is None:
        return GLSLVector([x, x, x, x])