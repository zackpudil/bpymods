from ..types import gen_type
from ..utils import reduce_exec_to_comps

def clamp(v, a, b):
    return __op__((v, a, b), lambda x, y, z: max(min(x, z), y))

def mod(v, a):
    return __op__((v, a), lambda x, y: x % y)

def max(v, w):
    return __op__((v, w), lambda x, y: x if x > y else y)

def min(v, w):
    return __op__((v, w), lambda x, y: x if x < y else y)

def step(e, v):
    return __op__((e, v), lambda x, y: 0 if y < x else 1)

def mix(v, w, a):
    return __op__((v, w, a), lambda x, y, b: x*(1 - b) + y*b)

def smoothstep(el, eh, v):
    return __op__((el, eh, v), ___smoothstep__)

def ___smoothstep__(e1, e2, x):
    t = clamp((x - e1)/(e2 - e1), 0, 1)
    return t*t*(3.0 - 2.0*t)

def __op__(vs, op):
    return gen_type(vs, reduce_exec_to_comps(vs, op))
