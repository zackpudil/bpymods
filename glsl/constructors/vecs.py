from ..types import GLSLVector
from ..utils import isValid, isVec

def vec2(x, y=None):
    if not isValid(y):
        return GLSLVector([x, x])

    return GLSLVector([x, y])

def vec3(x, y=None, z=None):
    if isValid(y) and isValid(z):
        return GLSLVector([x, y, z])
    elif isValid(y):
        if isVec(x):
            return GLSLVector(x.coords + [y])
        elif isVec(y):
            return GLSLVector([x] + y.coords)

    if not isValid(y) and not isValid(z):
        return GLSLVector([x, x, x])

def vec4(x, y=None, z=None, w=None):
    print(str(x))
    print(str(y))
    if isValid(y) and isValid(z) and isValid(w):
        return GLSLVector([x, y, z, w])

    if isValid(y) and isValid(z):
        if isVec(x):
            return GLSLVector(x.coords + [y, z])
        elif isVec(y):
            return GLSLVector([x] + y.coords + [z])
        elif isVec(z):
            return GLSLVector([x, y] + z.coords)

    if isValid(y):
        if isVec(x) and isVec(y):
            return GLSLVector(x.coords + y.coords)
        elif isVec(x):
            return GLSLVector(x.coords + [y])
        elif isVec(y):
            return GLSLVector([x] + y.coords)

    if not isValid(y) and not isValid(z) and not isValid(w):
        return GLSLVector([x, x, x, x])