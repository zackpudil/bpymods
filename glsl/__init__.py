from mathutils import Vector

from .types import *
from .constructors import *
from .operations import *
from .compiler import *


def to_glsl_vector(v):
    return vec3(v.x, v.z, v.y)


def to_vector(v):
    return Vector([v.x, v.z, v.y])