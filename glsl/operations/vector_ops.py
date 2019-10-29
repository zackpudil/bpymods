from ..utils import isVec
from ..types import GLSLVector
from math import sqrt

def length(x):
    return sqrt(sum((x*x).coords))

def dot(x, y):
    return sum((x*y).coords)

def clamp(x, a, b):
    if isVec(x):
        nx = []
        for i in range(0, len(x.coords)):
            if isVec(a):
                nx.append(clamp(x.coords[i], a.coords[i], b.coords[i]))
            else:
                nx.append(clamp(x.coords[i], a, b))
        return GLSLVector(nx)

    return max(min(x, b), a)

def mod(x, m):
    if isVec(x):
        if isVec(m):
            return GLSLVector([mod(c, m) for c, b in zip(x.coords, m.coords)])
        else:
            return GLSLVector(list(map(lambda c: mod(c, m), x.coords)))
    return x % m

def normalize(x):
    return GLSLVector(list(map(lambda c: c/length(x), x.coords)))