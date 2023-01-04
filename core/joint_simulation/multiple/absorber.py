import os.path

from core.joint_simulation import single
from core.util.cst import modeler as c_modeler
from core.joint_simulation import result as j_result


# ！！！: 返回的 info 标准：
# info 是一个信息字典， 用于返回这一次仿真中所有的数据信息
# 其中包括
# info["struct_param"] : 结构参数信息， 结构参数本身也是一个字典
# info["matrix_data"]     : 矩阵数据信息，可能是一个元组，因为可能有多层矩阵
# info["struct_name"]  : 结构的器件和名称信息，是一个元组
# info["sParam"]       : S 参数数据信息，是一个字典

# 竖条
def vertical_bar(file_name, batch=1, dir_project="absorber", freq_low=1, freq_high=5, isStart=True, cst_object=None):
    if isStart is True:
        cst_env, mws, cst_file_path = c_modeler.initial.create_new_mws_project(
            file_name, "template_unit_cell", freq_low, freq_high, dir_project)
        cst_object = (cst_env, mws, cst_file_path)
    else:
        cst_env, mws, cst_file_path = cst_object

    # n_size: 64
    # 数据量较少 不用分batch
    # l/2: 8~30,
    # w/2: 2~8,

    n_size = 64
    t = 0.58
    th = 2.4
    index = 0

    for w2 in range(2, 9):
        for l2 in range(8, 32):
            l = l2 * 2
            w = w2 * 2
            index = index + 1
            info = single.absorber.vertical_bar(mws, cst_file_path, n_size, l, w, t, th)
            j_result.info.handle_by_layer(batch, index, info, layer=1, dir_project=os.path.join(dir_project, file_name),
                                          mtype="absorber")

    return cst_object


# 十字
def cross(file_name, batch=1, dir_project="absorber", freq_low=1, freq_high=5, isStart=True, cst_object=None):
    if isStart is True:
        cst_env, mws, cst_file_path = c_modeler.initial.create_new_mws_project(
            file_name, "template_unit_cell", freq_low, freq_high, dir_project)
        cst_object = (cst_env, mws, cst_file_path)
    else:
        cst_env, mws, cst_file_path = cst_object

    # n_size: 64
    # 数据量较少 不用分batch
    # l/2: 8~30,
    # w/2: 2~8,

    n_size = 64
    t = 0.58
    th = 2.4
    index = 0

    for w2 in range(2, 9):
        for l2 in range(8, 32):
            l = l2 * 2
            w = w2 * 2
            index = index + 1
            info = single.absorber.cross(mws, cst_file_path, n_size, l, w, t, th)
            j_result.info.handle_by_layer(batch, index, info, layer=1, dir_project=os.path.join(dir_project, file_name),
                                          mtype="absorber")

    return cst_object
