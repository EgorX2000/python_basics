import itertools

people = sorted([input() for _ in range(int(input()))])
print(*[str(combination).removeprefix("(").removesuffix(")").replace("'", "") for combination
        in list(itertools.permutations(people, 3))], sep="\n")
