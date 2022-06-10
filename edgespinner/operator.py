import bpy
import bmesh
import logging

from .logic import EdgeSpinner
from .overrides import override_implicit_surface, TRIANGLE_SIZE, RAY_ORIGIN, RAY_DIRECTION


class EdgeSpinnerOperator(bpy.types.Operator):
    bl_idname = "objects.edge_spin_surface"
    bl_label = "Marching Triangles"

    timer = None
    object = None
    mesh = None
    bm = None

    edge_spinner = None

    def modal(self, context, event):
        try:
            if event.type == 'ESC':
                self.cancel(context)
                return {'FINISHED'}

            if event.type == 'TIMER':
                self.bm = self.edge_spinner.add_face(self.bm)
                bmesh.update_edit_mesh(self.mesh)

                self.bm = self.edge_spinner.remove_orphaned_verts(self.bm)
                bmesh.update_edit_mesh(self.mesh)

                self.bm = self.edge_spinner.merge_neighbor_verts(self.bm)
                bmesh.update_edit_mesh(self.mesh)

                self.bm = self.edge_spinner.remove_invalid_faces(self.bm)
                bmesh.update_edit_mesh(self.mesh)

                self.bm = self.edge_spinner.remove_orphaned_edges(self.bm)
                bmesh.update_edit_mesh(self.mesh)

                self.edge_spinner.next()
            return {'PASS_THROUGH'}
        except Exception as e:
            logging.exception(e)
            return {'FINISHED'}

    def execute(self, context):
        try:
            context.window_manager.modal_handler_add(self)
            self.timer = context.window_manager.event_timer_add(
                time_step=0.0001, window=context.window)

            if 'MarchingTriangles' in bpy.data.objects:
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.data.objects.remove(
                    bpy.data.objects['MarchingTriangles'], do_unlink=True)

            self.mesh = bpy.data.meshes.new('MarchingTriangles')
            self.object = bpy.data.objects.new('MarchingTriangles', self.mesh)
            context.collection.objects.link(self.object)

            self.object.select_set(True)
            context.view_layer.objects.active = self.object

            bpy.ops.object.mode_set(mode='EDIT')

            self.bm = bmesh.from_edit_mesh(self.mesh)

            self.edge_spinner = EdgeSpinner(override_implicit_surface, TRIANGLE_SIZE)
            self.bm = self.edge_spinner.add_initial_face(self.bm, RAY_ORIGIN, RAY_DIRECTION)

            bmesh.update_edit_mesh(self.mesh)

            return {'RUNNING_MODAL'}
        except Exception as e:
            logging.exception(e)
            return {'RUNNING_MODAL'}

    def cancel(self, context):
        context.window_manager.event_timer_remove(self.timer)
        self.bm.free()
        print('\n========EdgeSpin Done=========')
