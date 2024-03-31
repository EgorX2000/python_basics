import numpy as np


def snake(m, n, direction="H"):
    if direction == "H":
        matrix = np.arange(1, m * n + 1, dtype="int16").reshape((n, m))
        for i in range(1, n, 2):
            matrix[i] = matrix[i][-1::-1]
    elif direction == "V":
        matrix = np.arange(1, m * n + 1, dtype="int16").reshape((m, n))
        matrix = np.rot90(matrix)
        for i in range(n // 2):
            for j in range(0, m, 2):
                matrix[i][j], matrix[-i - 1][j] = matrix[-i - 1][j], matrix[i][j]

    return matrix
