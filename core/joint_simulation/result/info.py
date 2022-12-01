from core.joint_simulation.result import index as j_index, matrix as j_matrix, sParam as j_sParam


# AT用
# info 处理函
def handle_by_layer(batch, index, info, layer, dir_project):
    print("log-batch: " + str(batch) + " index: " + str(index))

    # index 数据保存
    struct_name = info["struct_name"]
    struct_param = info["struct_param"]
    j_index.save(batch, index, struct_name, struct_param, dir_project=dir_project)

    # 按层保存矩阵图像和数据
    AT_mat = info["matrix_data"]
    j_matrix.save_pic_by_layer(batch, AT_mat, layer=layer, dir_project=dir_project, prefix=str(index))
    j_matrix.save_data_by_layer(batch, AT_mat, layer=layer, dir_project=dir_project, prefix=str(index))

    sParam_AT_data = info["sParam"]
    j_sParam.save_all_Zmaxin(batch, sParam_AT_data, dir_project=dir_project, prefix=str(index))
