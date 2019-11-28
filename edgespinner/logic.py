from mathutils import Vector

from numpy import arange
from bpy_polly import get_verts_from_linked_faces, is_face_overlapping_others, is_point_in_triangles
from isf import trace_surface, get_normal, get_surface_point, get_tangent
import bmesh


class EdgeSpinner:
    ignore_indexes = []
    iteration = 0
    passes = 0
    triangle_size = 0.1
    sdf = None

    active_edge = None
    vert_new = None
    face_new = None

    def __init__(self, sdf, triangle_size):
        self.triangle_size = triangle_size
        self.sdf = sdf
        self.ignore_indexes = []
        self.iteration = 0

    def get_active_edge(self, edges):
        for e in edges: e.select = False

        first_pass = [e for e in edges if e.is_boundary and e.index not in self.ignore_indexes]
        if len(first_pass) != 0:
            first_pass[0].select = True
            return first_pass[0]

        self.ignore_indexes = []
        self.iteration = 0
        self.passes += 1

        second_pass = [e for e in edges if e.is_boundary]
        if len(second_pass) != 0:
            second_pass[0].select = True
            return second_pass[0]

        raise Exception('We done?')

    def get_initial_point(self, s, triangle_size):
        edge_cos = [v.co for v in self.active_edge.verts]

        vinit = [fe for fe in self.active_edge.link_faces[0].verts if fe.co not in edge_cos]

        pinit = vinit[0].co.copy()
        return s + triangle_size * (s - pinit).normalized()

    def add_face(self, bm):
        self.active_edge = self.get_active_edge(bm.edges)
        s = (self.active_edge.verts[0].co + self.active_edge.verts[1].co) / 2

        pinit = Vector.Fill(3)
        for i in arange(0, self.triangle_size, self.triangle_size / 8.0).tolist():
            pinit = self.get_initial_point(s, self.triangle_size - i)
            pinit = trace_surface(pinit, -get_normal(pinit, self.sdf), self.sdf, self.triangle_size - i)

            snormal = get_normal(s, self.sdf)
            pnormal = get_normal(pinit, self.sdf)

            a = snormal.angle(pnormal)
            if a <= 0.4:
                break

        self.vert_new = bm.verts.new(pinit)
        self.face_new = bm.faces.new([self.vert_new, self.active_edge.verts[0], self.active_edge.verts[1]])

        return bm

    def remove_orphaned_verts(self, bm):
        for v in bm.verts:
            if len(v.link_faces) == 0:
                bm.verts.remove(v)

        return bm

    def merge_neighbor_verts(self, bm):
        verts = [v for v in bm.verts if self.vert_new not in get_verts_from_linked_faces(v)]
        ovs = [ov for ov in verts if (ov.co - self.vert_new.co).length < self.triangle_size - self.triangle_size / 2.0]

        if len(ovs) > 0:
            self.ignore_indexes.append(self.active_edge.index)
            center = sum([self.vert_new.co] + [v.co for v in ovs], Vector.Fill(3)) / (len(ovs) + 1)
            trace_surface(center, -get_normal(center, self.sdf), self.sdf, self.triangle_size)
            bmesh.ops.pointmerge(bm, verts=[self.vert_new] + ovs, merge_co=center)

        return bm

    def remove_invalid_faces(self, bm):
        if is_point_in_triangles(bm.faces, self.vert_new.co):
            self.ignore_indexes.append(self.active_edge.index)
            bm.verts.remove(self.vert_new)
        elif is_face_overlapping_others(bm.faces, self.face_new):
            self.ignore_indexes.append(self.active_edge.index)
            bm.verts.remove(self.vert_new)

        return bm

    def remove_orphaned_edges(self, bm):
        orphaned_edges = [e for e in bm.edges if len(e.link_faces) == 0]
        if len(orphaned_edges) != 0:
            for e in orphaned_edges: bm.edges.remove(e)

        return bm

    def add_initial_face(self, bm):
        p0 = get_surface_point(self.sdf)

        normal = get_normal(p0, self.sdf)
        tangent = get_tangent(normal)
        bitangent = normal.cross(tangent)

        s = self.triangle_size
        p1 = trace_surface(p0 + s * tangent, -get_normal(p0 + s * tangent, self.sdf), self.sdf, s)
        p2 = trace_surface(p0 + s * bitangent, -get_normal(p0 + s * bitangent, self.sdf), self.sdf, s)

        v0 = bm.verts.new(p0)
        v1 = bm.verts.new(p1)
        v2 = bm.verts.new(p2)
        bm.faces.new([v1, v2, v0])

        return bm

    def next(self):
        self.iteration += 1
        print(self.passes, self.iteration, len(self.ignore_indexes))