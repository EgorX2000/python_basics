import pandas as pd


def length_stats(string):
    string = "".join(char for char in string if char.isalpha() or char == " ")
    string = sorted({word.lower() for word in string.split()})
    odd = pd.Series([len(word) for word in string if len(word) % 2 != 0], [
                    word for word in string if len(word) % 2 != 0], dtype="int64")
    even = pd.Series([len(word) for word in string if len(word) % 2 == 0], [
                     word for word in string if len(word) % 2 == 0], dtype="int64")
    return odd, even
