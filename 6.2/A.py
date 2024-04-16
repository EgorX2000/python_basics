import pandas as pd


def length_stats(string):
    string = "".join(char for char in string if char.isalpha() or char == " ")
    string = sorted({word.lower() for word in string.split()})
    return pd.Series([len(word) for word in string], string)
