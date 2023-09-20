def p(n):
    if len(n) % 2 == 0:
        if n[0: len(n) // 2] == n[-1: len(n) // 2 - 1: -1]:
            return 1
        else:
            return 0
    elif len(n) > 1:
        if n[0: len(n) // 2 + 1] == n[-1: len(n) // 2 - 1: -1]:
            return 1
        else:
            return 0
    else:
        return 1


n = int(input())

count = 0
for i in range(n):
    if p(input()):
        count += 1

print(count)
