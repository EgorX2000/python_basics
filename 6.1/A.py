import math


x = float(input())
print(math.log(math.pow(x, 3 / 16), 32) +
      x ** math.cos(math.pi * x / 2 / math.e) -
      math.pow(math.sin(x / math.pi), 2))
