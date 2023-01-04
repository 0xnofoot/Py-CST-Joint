import numpy as np
from core.util.matrix.operation import bool as m_bool


# 获取矩阵中 每一个块周围八个块的数据信息
def get_round_bricks(brick, n_size):
    x = brick[0]
    y = brick[1]
    round_bricks = list()
    round_bricks.append((x - 1, y - 1))
    round_bricks.append((x - 1, y))
    round_bricks.append((x - 1, y + 1))
    round_bricks.append((x, y - 1))
    round_bricks.append((x, y + 1))
    round_bricks.append((x + 1, y - 1))
    round_bricks.append((x + 1, y))
    round_bricks.append((x + 1, y + 1))

    def limit_filter(brick):
        if 0 <= brick[0] < n_size and 0 <= brick[1] < n_size:
            return True
        return False

    round_bricks = list(filter(lambda b: limit_filter(b), round_bricks))

    return round_bricks


# 矩阵过滤
def filter_by_around(matrix, step=1):
    for i in range(step):
        ############################################
        for brick, value in np.ndenumerate(matrix):
            round_bricks = get_round_bricks(brick, 64)
            round_sum = sum(map(lambda b: matrix[b], round_bricks))

            if value == 0 and round_sum >= 4:
                matrix[brick] = 1
            elif value == 1 and round_sum < 5:
                matrix[brick] = 0

        ############################################
        for brick, value in np.ndenumerate(matrix):
            round_bricks = get_round_bricks(brick, 64)
            round_sum = sum(map(lambda b: matrix[b], round_bricks))

            if value == 1 and round_sum < 5:
                matrix[brick] = 0
            elif value == 0 and round_sum >= 4:
                matrix[brick] = 1

    return matrix


# 环绕生长，用于生成聚合度高的矩阵数据
def around_growth(n_size, count, step, ac_brick_initial=None):
    matrix = np.zeros((n_size, n_size))
    ac_count = count
    ac_bricks = set()
    iac_bricks = set()

    if ac_brick_initial is None:
        # ac_brick_initial = (np.random.randint(0, n_size), np.random.randint(0, n_size))
        ac_brick_initial = (int(n_size / 2), int(n_size / 2))

    matrix[ac_brick_initial] = 1

    ac_bricks.add(ac_brick_initial)

    def active_brick():
        if len(ac_bricks) != 0:
            ac_brick = ac_bricks.pop()
        else:
            ac_brick = iac_bricks.pop()
        iac_bricks.add(ac_brick)

        round_bricks = get_round_bricks(ac_brick, n_size)

        def ac_filter(brick):
            if brick not in ac_bricks and brick not in iac_bricks:
                return True
            return False

        round_bricks = list(filter(lambda b: ac_filter(b), round_bricks))
        np.random.shuffle(round_bricks)
        if len(round_bricks) < ac_count:
            n = len(round_bricks)
        else:
            n = ac_count
        round_bricks = round_bricks[:n]

        return round_bricks

    for i in range(step):
        ac_round_bricks = active_brick()
        for b in ac_round_bricks:
            matrix[b] = 1
            ac_bricks.add(b)

    return matrix


def poly_matrix(ratio):
    adds = int(11 * ratio)
    subts = 11 - adds

    matrix1 = around_growth(64, 1, 100, ac_brick_initial=(24, 24))
    matrix2 = around_growth(64, 1, 100, ac_brick_initial=(24, 40))
    matrix3 = around_growth(64, 1, 100, ac_brick_initial=(40, 40))
    matrix4 = around_growth(64, 1, 100, ac_brick_initial=(40, 24))
    matrix5 = around_growth(64, 1, 100, ac_brick_initial=(32, 24))
    matrix6 = around_growth(64, 1, 100, ac_brick_initial=(24, 32))
    matrix7 = around_growth(64, 1, 100, ac_brick_initial=(32, 40))
    matrix8 = around_growth(64, 1, 100, ac_brick_initial=(40, 32))
    matrix9 = around_growth(64, 1, 100, ac_brick_initial=(40, 32))
    matrix10 = around_growth(64, 1, 100, ac_brick_initial=(40, 32))
    matrix11 = around_growth(64, 1, 100, ac_brick_initial=(40, 32))
    matrix12 = around_growth(64, 1, 100, ac_brick_initial=(40, 32))

    matrix_list = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6,
                   matrix7, matrix8, matrix9, matrix10, matrix11, matrix12]

    np.random.shuffle(matrix_list)
    matrix = matrix_list.pop()

    i = 0
    for m in matrix_list:
        if i < adds:
            matrix = m_bool.add(matrix, m)
        else:
            matrix = m_bool.subtract(matrix, m)
        i = i + 1

    return matrix
# for i in range(500):
#     matrix = np.random.randint(0, 2, (64, 64))
#     matrix = m_fun.filter_by_around(matrix, step=4)
#     m = np.sum(matrix)
#     if m > 400:
#         m_show.save_show_pic_rat90(matrix, isSave=True, dir="1", name=str(i), isShow=False)

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
