import math
import sys

for s in sys.stdin:
    nums = list(map(int, s.split()))
    print(math.gcd(*nums))
