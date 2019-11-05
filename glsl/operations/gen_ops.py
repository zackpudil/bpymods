from ..types import GLSLVector, gen_type
from ..utils import reduce_exec_to_comps

def clamp(v, a, b):
    return gen_type(reduce_exec_to_comps((v, a, b), lambda x, y, z: max(min(x, z), y)))

def mod(v, a):
    return gen_type(reduce_exec_to_comps((v, a), lambda x, y: x % y))

def max(v, w):
    return gen_type(reduce_exec_to_comps((v, w), lambda x, y: x if x > y else y))

def min(v, w):
    return gen_type(reduce_exec_to_comps((v, w), lambda x, y: x if x < y else y))

def smoothstep(edgeLow, edgeHigh, v):
    return gen_type(reduce_exec_to_comps((v, edgeLow, edgeHigh), lambda x, e1, e2: _interpolate_smoothstep(x, e1, e2)))

def _interpolate_smoothstep(x, e1, e2):
    t = clamp((x - e1)/(e2 - e1), 0, 1)
    return t*t*(3.0 - 2.0*t)
