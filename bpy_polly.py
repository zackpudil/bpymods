from functools import reduce
from math import pi


def get_verts_from_linked_faces(vert):
    return reduce(lambda a, b: a + list(b.verts), vert.link_faces, [])


def is_face_overlapping_others(faces, face):
    faces_to_check = [f for f in faces
                      if f != face and (face.calc_center_median() - f.calc_center_median()).length < 0.5]

    for f in faces_to_check:
        if is_point_in_triangle(f, face.calc_center_median()) \
                or is_point_in_triangle(face, f.calc_center_median()):
            return True

    return False


def is_point_in_triangles(faces, point):
    faces_to_check = [f for f in faces
                      if point not in [v.co for v in f.verts]
                      and (point - f.calc_center_bounds()).length < 0.3]

    for cf in faces_to_check:
        if is_point_in_triangle(cf, point):
            return True

    return False


def is_point_in_triangle(face, point):
    [a, b, c] = [v.co - point for v in face.verts]
    angle_a = a.angle(b) if a.length != 0 and b.length != 0 else 0
    angle_b = b.angle(c) if b.length != 0 and c.length != 0 else 0
    angle_c = c.angle(a) if c.length != 0 and a.length != 0 else 0

    angle = angle_a + angle_b + angle_c
    if abs(angle - 2 * pi) < 0.2:
        return True

    return False