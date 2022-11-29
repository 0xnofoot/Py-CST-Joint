def add(matrix1, *matrix2):
    for matrix in matrix2:
        matrix1 = matrix1 + matrix
        matrix1[matrix1 > 1] = 1
    return matrix1


def subtract(matrix1, *matrix2):
    for matrix in matrix2:
        matrix1 = matrix1 - matrix
        matrix1[matrix1 < 0] = 0
    return matrix1
