n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

for i in range(n + 1):
    if k1 * (i) + k2 * (n - i) == m * n:
        break

print(i, n - i)
