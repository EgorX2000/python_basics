import itertools

n = int(input())
letters = list()
for _ in range(n):
    letters.append(list(set(input().split(sep="-"))))

answers = list(itertools.product(*letters))
for ans in sorted(answers):
    print(*ans, sep="")
