import numpy as np


def make_board(n):
    matrix = np.indices((n, n)).sum(axis=0) % 2
    return np.array(np.rot90(matrix), dtype="int8")
