from math import cos, sin
from glsl import mat2, clamp, mix


def rotate(a):
    c = cos(a)
    s = sin(a)

    return mat2(c, s, -s, c)


def smooth_min(a, b, k):
    h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0)
    return mix(b, a, h) - k * h * (1.0 - h)


def smooth_max(a, b, k):
    h = max(k - abs(a - b), 0.0)/k
    return max(a, b) - h*h*k*(1/4)