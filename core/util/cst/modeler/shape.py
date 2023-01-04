from core.util.cst.vb import modeler
import numpy as np


def create_brick(mws, name, material, x1_range, x2_range, y1_range, y2_range,
                 z1_range, z2_range, component="component1"):
    modeler.create_brick(mws.modeler, name, material, x1_range, x2_range, y1_range, y2_range,
                         z1_range, z2_range, component)


def delete_solid(mws, component, name):
    modeler.delete_solid(mws.modeler, component, name)


# 通过矩阵生成CST模型，以（0，0）为中心
def create_grid_by_matrix(mws, material, matrix, step, z1, z2, component, name):
    x_size, y_size = np.shape(matrix)
    x_start = -x_size / 2 * step
    y_start = -y_size / 2 * step

    count = 0
    for index, value in np.ndenumerate(matrix):
        if value == 0:
            continue
        count = count + 1
        x, y = index
        x1 = x_start + x * step
        x2 = x1 + step
        y1 = y_start + y * step
        y2 = y1 + step

        if count == 1:
            create_brick(mws, name, material, x1, x2, y1, y2, z1, z2, component)
        else:
            i_name = name + "_grid_" + str(x) + "_" + str(y)
            create_brick(mws, i_name, material, x1, x2, y1, y2, z1, z2, component)
            modeler.bool_add(mws.modeler, component, name, component, i_name)

    return component, name
