from ..types import GLSLVector
from math import sqrt


def length(x):
    return sqrt(sum((x*x).coordinates))


def dot(x, y):
    return sum((x*y).coordinates)


def normalize(v):
    return GLSLVector([x / length(v) for x in v.coordinates])
