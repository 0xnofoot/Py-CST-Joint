from util.matrix.old import simulation_matrix

import joint_simulation
from core.util.cst import modeler as c_modl
from core import global_var

WORK_HOME = global_var.WORK_HOME


def create_door_polymerize_random_project(file_name):
    x_size = 64
    y_size = 64
    sub_t = 20
    metal_t = 0.2

    cst_env, mws = c_modl.initial.create_new_mws_project(file_name, "template_unit_cell", 0.2, 2, "Door&pm_random")

    c_modl.material.define_material(mws, "Polyimide", 3.0, 1.0, 0.008, folder="custom dielectric material",
                                    color=(0.89, 1, 0.9569))
    c_modl.material.load_material(mws, "Aluminum")
    c_modl.shape.create_brick(mws, "substrate_mid", "custom dielectric material/Polyimide", 0, x_size * 2, 0,
                              y_size * 2,
                              0, sub_t, component="sub")

    matrix = simulation_matrix.door_polymerize_random(x_size=x_size, y_size=y_size, pm_count=3, pm_step=20,
                                                      operands=50,
                                                      ratio=0.98)
    c_modl.view.zoom_to_structure(mws)
    c_modl.shape.create_grid_by_matrix(mws, "Aluminum", matrix, 2, sub_t, sub_t + metal_t, component="metal_up")


joint_simulation.single.AT.dorr("AT-simulation-test", 64, 53, 8, 5, 10)
