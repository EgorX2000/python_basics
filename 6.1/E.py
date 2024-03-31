import math


dec = list(map(float, input().split()))
pol = list(map(float, input().split()))

pd = [pol[0] * math.cos(pol[1]), pol[0] * math.sin(pol[1])]

print(math.dist((dec[0], dec[1], 0), (pd[0], pd[1], 0)))
