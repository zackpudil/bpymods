from .logic import EdgeSpinner
import importlib
import bpy

def edge_spin_surface(surface_function, triangle_size):
    import edgespinner.overrides
    edgespinner.overrides.override_implicit_surface = surface_function
    edgespinner.overrides.TRIANGLE_SIZE = triangle_size

    import edgespinner.operator
    importlib.reload(edgespinner.operator)
    try:
        bpy.utils.unregister_class(edgespinner.operator.EdgeSpinnerOperator)
    except:
        print('Unable to unregister class, ignore if first run')

    global override_implicit_surface
    override_implicit_surface = surface_function

    global TRIANGLE_SIZE
    TRIANGLE_SIZE = triangle_size

    bpy.utils.register_class(edgespinner.operator.EdgeSpinnerOperator)
    print('\n========EdgeSpin Start=========')
    bpy.ops.objects.edge_spin_surface()
