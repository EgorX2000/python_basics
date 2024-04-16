import pandas as pd


def get_long(data, min_length=5):
    ans = pd.Series(dtype="int64")
    for i in data.index:
        if data.loc[i] >= min_length:
            ans[i] = data.loc[i]
    return ans
