import numpy as np


# dorr: double_open_rectangular_ring
def dorr_random(x_size, y_size):
    matrix = np.zeros((x_size, y_size))

    if x_size == y_size:
        n = x_size
    else:
        n = min(x_size, y_size)

    l = np.random.randint(45, 55)  # l 90 ~ 110
    p1 = int((n - l) / 2)
    matrix[p1:p1 + l, p1:p1 + l] = 1

    w = np.random.randint(8, 11)  # w 15 ~ 20
    p2 = l - 2 * w
    matrix[p1 + w:p1 + w + p2, p1 + w:p1 + w + p2] = 0

    s = np.random.randint(5, 15)  # s 5 ~ 20
    g = np.random.randint(10, 20)  # g 20 ~ 40
    p3 = p1 + w + s
    matrix[p1 + l - w:p1 + l, p3:p3 + g] = 0
    matrix[p1:p1 + w, p1 + l - w - s - g: p1 + l - w - s] = 0

    return matrix
