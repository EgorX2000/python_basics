import math

nums = list(map(float, input().split()))
print(math.pow(math.prod(nums), 1 / len(nums)))
