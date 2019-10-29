from .types import GLSLVector

def isValid(a):
    return a is not None

def isVec(a):
    return isinstance(a, GLSLVector)