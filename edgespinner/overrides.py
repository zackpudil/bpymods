from math import sqrt
from mathutils import Vector


def override_implicit_surface(p):
    return sqrt((p.x*p.x + p.y*p.y + p.z*p.z)) - 1.0


RAY_ORIGIN = Vector([0, 0, -3])
RAY_DIRECTION = Vector([0, 0, 1])

TRIANGLE_SIZE = 0.1