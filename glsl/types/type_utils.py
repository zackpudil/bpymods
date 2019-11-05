from .glsl_vector import GLSLVector

def gen_type(a):
    return GLSLVector(a) if isinstance(a, list) and len(a) >= 2 else a

