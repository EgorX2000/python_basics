import numpy as np
import pandas as pd


def values(func, start, end, step):
    return pd.Series(map(func, np.arange(start, end + step, step)), np.arange(start, end + step, step), dtype='float64')


def min_extremum(data):
    return min(data[data == min(data)].index)


def max_extremum(data):
    return max(data[data == max(data)].index)
