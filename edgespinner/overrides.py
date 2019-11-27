from math import sqrt


def override_implicit_surface(p):
    return sqrt((p.x*p.x + p.y*p.y + p.z*p.z)) - 1.0


TRIANGLE_SIZE = 0.1