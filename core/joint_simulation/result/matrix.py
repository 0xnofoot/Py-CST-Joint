import os
import numpy as np

from core.util.matrix import operation as m_operation
from core import global_var

output_dir = global_var.output_dir


def save_data(matrix, dir, name):
    save_dir = os.path.join(output_dir, dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, name)
    np.savetxt(file_path, matrix, fmt="%d", delimiter=" ")


def save_data_AT(batch, AT_mat, dir="AT", prefix="", suffix=".txt"):
    AT_mat_up = AT_mat[0]
    AT_mat_down = AT_mat[1]
    save_data(AT_mat_up, os.path.join(dir, str(batch) + "_batch", "matrix", "data", "AT_up"),
              prefix + "_" + "mat_data" + suffix)
    save_data(AT_mat_down, os.path.join(dir, str(batch) + "_batch", "matrix", "data", "AT_down"),
              prefix + "_" + "mat_data" + suffix)


def save_pic(matrix, dir, name):
    m_operation.show.save_show_pic_rat90(matrix, isSave=True, dir=dir, name=name, isShow=False)


def save_pic_AT(batch, AT_mat, dir="AT", prefix="", suffix=""):
    AT_mat_up = AT_mat[0]
    AT_mat_down = AT_mat[1]

    save_pic(AT_mat_up, os.path.join(dir, str(batch) + "_batch", "matrix", "pic", "AT_up"),
             prefix + "_" + "mat_pic" + suffix)
    save_pic(AT_mat_down, os.path.join(dir, str(batch) + "_batch", "matrix", "pic", "AT_down"),
             prefix + "_" + "mat_pic" + suffix)
