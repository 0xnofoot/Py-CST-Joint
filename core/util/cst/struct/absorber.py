from core.util.cst import modeler as c_modeler


def generalization(mws, material, matrix, step, z1, z2, component="Metal", name="default"):
    return c_modeler.shape.create_grid_by_matrix(mws, material, matrix, step, z1, z2, component, name)
