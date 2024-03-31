import numpy as np


def stairs(vector):
    return np.array([np.roll(vector, i) for i in range(len(vector))])
