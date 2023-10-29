import itertools

purchases = list()
for _ in range(int(input())):
    purchases.extend(input().split(sep=", "))
purchases.sort()

print(*[str(combination).removeprefix("(").removesuffix(")").replace("'", "").replace(",", "") for combination
        in list(itertools.permutations(purchases, 3))], sep="\n")
