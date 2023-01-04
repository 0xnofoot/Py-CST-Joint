from core.util.matrix import operation as m_operation
from core import global_var
import numpy as np

output_dir = global_var.output_dir


# l 和 w 都必须是偶数
def vertical_bar(n_size, l, w):
    if l % 2 != 0:
        l = l + 1

    if w % 2 != 0:
        w = w + 1

    base = np.zeros((n_size, n_size))

    n_size_offset = int(n_size / 2)

    x1 = int(-(w / 2)) + n_size_offset
    x2 = int(w / 2) + n_size_offset
    y1 = int(-(l / 2)) + n_size_offset
    y2 = int(l / 2) + n_size_offset
    base[x1:x2, y1:y2] = 1

    return base


def cross(n_size, l, w):
    v_bar_mat = vertical_bar(n_size, l, w)
    h_bar_mat = np.rot90(v_bar_mat, 1)
    cross_mat = m_operation.bool.add(v_bar_mat, h_bar_mat)

    return cross_mat
