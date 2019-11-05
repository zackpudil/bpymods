from functools import reduce

def is_glsl_type(v):
    return hasattr(v, 'coords') and hasattr(v, 'cols')

def is_matrix(m):
    return hasattr(m, 'cols') and len(m.cols) > 1

def is_vector(v):
    return hasattr(v, 'cols') and len(v.cols) == 1

def reduce_exec_to_comps(vs, op):
    args = [v.coords if is_glsl_type(v) else [v] for v in vs]
    m = reduce(lambda a, b: a if a > len(b) else len(b), args, 0)
    spread = [x if len(x) == m else x*m for x in args]
    component_args = list(zip(*spread))

    if m > 1:
        return [op(*x) for x in component_args]

    return op(*component_args[0])
