from core.util.matrix import struct as m_struct, operation as m_operation
from core.util.cst import modeler as c_modeler, struct as c_struct, result as c_result


# ！！！: 返回的 info 标准：
# info 是一个信息字典， 用于返回这一次仿真中所有的数据信息
# 其中包括
# info["struct_param"] : 结构参数信息， 结构参数本身也是一个字典
# info["matrix_data"]     : 矩阵数据信息，是一个元组，因为可能有多层矩阵
# info["struct_name"]  : 结构器件和名称信息，是一个元组
# info["sParam"]       : S 参数数据信息，是一个字典

# 竖条
def vertical_bar(mws, cst_file_path, n_size, l, w, t, th, step=1):
    info = {}

    struct_param = {"n_size": n_size, "l": l, "w": w, "t": t, "th": th}
    info["struct_param"] = struct_param

    matrix = m_struct.absorber.vertical_bar(n_size, l, w)

    info["matrix_data"] = (matrix,)

    c_modeler.material.load_material(mws, "Gold")
    c_modeler.material.load_material(mws, "PTFE (lossy)")

    c_modeler.solver.boundary(mws, Zmin="electric")

    metal_sub_name = c_struct.substrate.brick_sub(mws, "Gold", n_size, n_size, 0, t, step, name="metal_sub")
    medium_sub_name = c_struct.substrate.brick_sub(mws, "PTFE (lossy)", n_size, n_size, t, t + th, step,
                                                   name="medium_sub")
    bar_name = c_struct.absorber.generalization(mws, "Gold", matrix, step, t + th, t + th + t, name="vertical_bar")
    info["struct_name"] = (metal_sub_name, medium_sub_name, bar_name)

    isComplete = c_modeler.solver.run(mws)

    if isComplete is not True:
        print("run failed")
        return

    # 返回 S 参数，对于单极化的吸收器来说，只需要一种 S参数的数据，SZmax(1),Zmax(1)
    sParam_Zmax1_Zmax1 = c_result.sParam.get_Zmax1_Zmax1(cst_file_path)
    sParam = {"Zmax1_Zmax1": sParam_Zmax1_Zmax1}
    info["sParam"] = sParam

    c_modeler.shape.delete_solid(mws, metal_sub_name[0], metal_sub_name[1])
    c_modeler.shape.delete_solid(mws, medium_sub_name[0], medium_sub_name[1])
    c_modeler.shape.delete_solid(mws, bar_name[0], bar_name[1])

    return info


# 十字
def cross(mws, cst_file_path, n_size, l, w, t, th, step=1):
    info = {}

    struct_param = {"n_size": n_size, "l": l, "w": w, "t": t, "th": th}
    info["struct_param"] = struct_param

    matrix = m_struct.absorber.cross(n_size, l, w)

    info["matrix_data"] = (matrix,)

    c_modeler.material.load_material(mws, "Gold")
    c_modeler.material.load_material(mws, "PTFE (lossy)")

    c_modeler.solver.boundary(mws, Zmin="electric")

    metal_sub_name = c_struct.substrate.brick_sub(mws, "Gold", n_size, n_size, 0, t, step, name="metal_sub")
    medium_sub_name = c_struct.substrate.brick_sub(mws, "PTFE (lossy)", n_size, n_size, t, t + th, step,
                                                   name="medium_sub")
    bar_name = c_struct.absorber.generalization(mws, "Gold", matrix, step, t + th, t + th + t, name="cross")
    info["struct_name"] = (metal_sub_name, medium_sub_name, bar_name)

    isComplete = c_modeler.solver.run(mws)

    if isComplete is not True:
        print("run failed")
        return

    # 返回 S 参数，对于单极化的吸收器来说，只需要一种 S参数的数据，SZmax(1),Zmax(1)
    sParam_Zmax1_Zmax1 = c_result.sParam.get_Zmax1_Zmax1(cst_file_path)
    sParam = {"Zmax1_Zmax1": sParam_Zmax1_Zmax1}
    info["sParam"] = sParam

    c_modeler.shape.delete_solid(mws, metal_sub_name[0], metal_sub_name[1])
    c_modeler.shape.delete_solid(mws, medium_sub_name[0], medium_sub_name[1])
    c_modeler.shape.delete_solid(mws, bar_name[0], bar_name[1])

    return info
