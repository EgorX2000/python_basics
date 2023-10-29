import itertools

n, m = int(input()), int(input())
length = len(str(n * m))
for i in range(n):
    line = list(itertools.product(range(1, m + 1), [i * m]))
    print(*list(f"{(elem[0] + elem[1]):>{length}}" for elem in line))
