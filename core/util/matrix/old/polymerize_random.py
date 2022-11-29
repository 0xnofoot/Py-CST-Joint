import numpy as np

import util.matrix.old.operation_matrix as op_matrix


def around_growth(ac_brick_initial, x_size, y_size, count, step):
    matrix = np.zeros((x_size, y_size))
    ac_count = count
    ac_bricks = set()
    iac_bricks = set()

    if ac_brick_initial is None:
        ac_brick_initial = (np.random.randint(0, x_size), np.random.randint(0, y_size))

    matrix[ac_brick_initial] = 1

    ac_bricks.add(ac_brick_initial)

    def active_brick():
        if len(ac_bricks) != 0:
            ac_brick = ac_bricks.pop()
        else:
            ac_brick = iac_bricks.pop()
        iac_bricks.add(ac_brick)

        round_bricks = op_matrix.get_round_bricks(ac_brick, x_size, y_size)

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
