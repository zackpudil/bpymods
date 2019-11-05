from ..types import GLSLVector
from math import sqrt

def length(x):
    return sqrt(sum((x*x).coords))

def dot(x, y):
    return sum((x*y).coords)

def normalize(v):
    return GLSLVector([x/length(v) for x in v.coords])