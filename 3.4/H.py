import itertools

porridges = [input() for _ in range(int(input()))]

n = int(input())
print(*list(itertools.islice(porridges * (n // len(porridges) + 1), n)), sep="\n")
