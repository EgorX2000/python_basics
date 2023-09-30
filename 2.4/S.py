n = int(input())

for i in range(n):
    for j in range(n):
        print(
            f"{min(i, j, n - i - 1, n - j - 1) + 1:>{len(str(n // 2 + n % 2))}}", end=" ")
    print()
