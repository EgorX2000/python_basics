import numpy as np


def rotate(matrix, angle):
    return np.rot90(matrix, -angle // 90)
