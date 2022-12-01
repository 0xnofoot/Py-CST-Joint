import sys
import os
import numpy as np

import global_var
from joint_simulation import multiple
from core.util.matrix.operation import fun as m_fun, show as m_show, bool as m_bool

# cst_object = multiple.AT.dorr("dorr_64x64_step", batch=5, dir_project="AT_dorr")

for i in range(500):
    matrix = np.random.randint(0, 2, (64, 64))
    matrix = m_fun.filter_by_around(matrix, step=4)
    m = np.sum(matrix)
    if m > 400:
        m_show.save_show_pic_rat90(matrix, isSave=True, dir="1", name=str(i), isShow=False)

    # matrix1 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(24, 24))
    # matrix2 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(24, 40))
    # matrix3 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(40, 40))
    # matrix4 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(40, 24))
    # matrix5 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(32, 24))
    # matrix6 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(24, 32))
    # matrix7 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(32, 40))
    # matrix8 = m_fun.around_growth(64, 1, 100, ac_brick_initial=(40, 32))
    # matrix_1 = m_bool.add(matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7, matrix8)
    # matrix_1 = m_fun.filter_by_around(matrix_1, step=2)
    #
    # matrix1 = m_fun.around_growth(64, 1, 30, ac_brick_initial=(32, 32))
    # matrix2 = m_fun.around_growth(64, 1, 30, ac_brick_initial=(32, 32))
    # matrix3 = m_fun.around_growth(64, 1, 30, ac_brick_initial=(32, 32))
    # matrix4 = m_fun.around_growth(64, 1, 30, ac_brick_initial=(32, 32))
    # matrix_2 = m_bool.add(matrix1, matrix2, matrix3, matrix4)
    # matrix_2 = m_fun.filter_by_around(matrix_2, step=1)
    #
    # matrix_3 = m_bool.subtract(matrix_1, matrix_2)
    # # matrix_3 = m_fun.filter_by_around(matrix_3, step=1)
    #
    # # m_show.save_show_pic_rat90(matrix11)
    # # m_show.save_show_pic_rat90(matrix22)
    #
    # m_show.save_show_pic_rat90(matrix_1, isSave=True, dir="1", name=str(i), isShow=False)
    # m_show.save_show_pic_rat90(matrix_2, isSave=True, dir="2", name=str(i), isShow=False)
    # m_show.save_show_pic_rat90(matrix_3, isSave=True, dir="3", name=str(i), isShow=False)

    # m_show.save_show_pic_rat90(matrix, isSave=True, dir="2", name=str(i), isShow=False)

    # matrix = m_fun.poly_matrix(0.7)
    # m_show.save_show_pic_rat90(matrix)
    # # m_show.save_show_pic_rat90(matrix, isSave=True, dir="1", name=str(1), isShow=False)
    #
    # matrix = m_fun.filter_by_around(matrix, step=2)
    # m_show.save_show_pic_rat90(matrix)
    # # m_show.save_show_pic_rat90(matrix, isSave=True, dir="2", name=str(1), isShow=False)
