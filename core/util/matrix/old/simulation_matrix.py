import numpy as np

import util.matrix.old.AT_create as AT_create
import util.matrix.old.polymerize_random as polymerize_random
import util.matrix.old.operation_matrix as op_matrix


def door_polymerize_random(x_size=64, y_size=64, pm_count=2, pm_step=20, operands=100, ratio=0.95):
    door_matrix = AT_create.dorr_random(x_size, y_size)
    matrix = door_matrix.copy()

    def get_poly_matrix():
        while True:
            ac_brick_initial = (np.random.randint(0, x_size), np.random.randint(0, y_size))
            if door_matrix[ac_brick_initial] == 1:
                break
        poly_matrix = polymerize_random.around_growth(ac_brick_initial, x_size, y_size, pm_count, pm_step)
        return poly_matrix

    operands_add = int(operands * ratio)
    operands_reduce = operands - operands_add
    operands_gcd = np.gcd(operands_add, operands_reduce)
    flag_add = operands_add / operands_gcd
    flag_reduce = operands_reduce / operands_gcd

    for i in range(operands):
        poly_matrix = get_poly_matrix()
        flag = i % (flag_add + flag_reduce)
        if flag < flag_add:
            matrix = op_matrix.add_bool(matrix, poly_matrix)
        else:
            matrix = op_matrix.reduce_bool(matrix, poly_matrix)

    for brick, value in np.ndenumerate(matrix):
        round_bricks = op_matrix.get_round_bricks(brick, x_size, y_size)
        round_sum = sum(map(lambda b: matrix[b], round_bricks))

        if value == 0 and round_sum > 5:
            matrix[brick] = 1
        elif value == 1 and round_sum < 4:
            matrix[brick] = 0

    return matrix
