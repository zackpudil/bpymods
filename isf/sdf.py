from glsl import clamp, dot, length, vec2


def capsule(p, a, b, r):
    pa = p - a
    ba = b - a
    h = clamp( dot(pa,ba)/dot(ba,ba), 0.0, 1.0 )
    return length( pa - ba*h ) - r


def torus(p, h):
    q = vec2(length(p.xz) - h.x, p.y)
    return length(q) - h.y


def box(p, b):
    q = abs(p) - b
    return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0)
