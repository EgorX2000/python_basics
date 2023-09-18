n = int(input())

current = target = 0
for i in range(1, n + 1):
    if current == target:
        print(i)
        current = 0
        target += 1
    else:
        print(i, end=" ")
        current += 1
