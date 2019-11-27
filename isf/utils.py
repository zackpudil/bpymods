from glsl import to_glsl_vector
from mathutils import Vector


def trace_surface(ro, rd, sdf, ts, ep=0.0001):
    t = 0
    for i in range(0, 200):
        d = sdf(to_glsl_vector(ro + rd * t))
        if abs(d) < ep:
            return ro + rd * t
        t += d

    if ts == 0:
        raise Exception('Cannot find initial surface point')

    return ro + rd * (ts / 8.0)


def get_surface_point(sdf):
    ro = Vector([0.0, -3, 0.0])
    rd = Vector([0, 1, 0]).normalized()
    return trace_surface(ro, rd, sdf, 0)


def get_normal(p, sdf):
    h = Vector([0.0001, 0.0])
    n = Vector([
        sdf(to_glsl_vector(p + h.xyy)) - sdf(to_glsl_vector(p - h.xyy)),
        sdf(to_glsl_vector(p + h.yxy)) - sdf(to_glsl_vector(p - h.yxy)),
        sdf(to_glsl_vector(p + h.yyx)) - sdf(to_glsl_vector(p - h.yyx)),
    ])

    return n.normalized()


def get_tangent(normal):
    return normal.cross(Vector([-normal.z, normal.x, normal.y]))