import pandas as pd


data = pd.read_csv("data.csv", )
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

print(data[(a1 <= data["x"]) & (data["x"] <= b1)
      & (a2 >= data["y"]) & (data["y"] >= b2)])
