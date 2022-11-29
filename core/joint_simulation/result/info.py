from core.joint_simulation.result import index as j_index, matrix as j_matrix, sParam as j_sParam


# AT用
# info 处理函数
def AT_handle(batch, index, info, dir):
    print("log-batch: " + str(batch) + " index: " + str(index))

    # index 数据保存
    struct_name = info["struct_name"]
    struct_param = info["struct_param"]
    j_index.save(batch, index, struct_name, struct_param, dir)

    # 保存矩阵图像和数据
    AT_mat = info["matrix_data"]
    j_matrix.save_pic_AT(batch, AT_mat, dir=dir, prefix=str(index))
    j_matrix.save_data_AT(batch, AT_mat, dir=dir, prefix=str(index))

    sParam_AT_data = info["sParam"]
    j_sParam.save_AT(batch, sParam_AT_data, dir, prefix=str(index))
