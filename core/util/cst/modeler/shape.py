from core.util.cst.vb import modeler
import numpy as np


def create_brick(mws, name, material, x1_range, x2_range, y1_range, y2_range,
                 z1_range, z2_range, component="component1"):
    modeler.create_brick(mws.modeler, name, material, x1_range, x2_range, y1_range, y2_range,
                         z1_range, z2_range, component)


def delete_solid(mws, component, name):
    modeler.delete_solid(mws.modeler, component, name)


def create_grid_by_matrix(mws, material, matrix, step, z1_range, z2_range, component):
    x_size, y_size = np.shape(matrix)
    x_start = 0
    y_start = x_size * step

    count = 0
    for index, value in np.ndenumerate(matrix):
        if count % 1000 == 0:
            mws.save()
        count = count + 1
        if value == 0:
            continue
        y, x = index
        name = "grid_" + str(x) + "_" + str(y)
        x1_range = x_start + x * step
        x2_range = x1_range + step
        y1_range = y_start - y * step
        y2_range = y1_range - step

        create_brick(mws, name, material, x1_range, x2_range, y1_range, y2_range, z1_range, z2_range, component)
