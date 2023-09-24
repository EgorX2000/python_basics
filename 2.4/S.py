n = int(input())

mas = [0] * n
for i in range(n):
    mas[i] = [0] * n

k = n
m = len(str(n // 2 + 1))
for i in range(n):
    for j in range(n):
        if i == j:
            mas[i][j] = mas[n - 1 - i][j] = mas[i][n - 1 -
                                                   j] = mas[n - 1 - i][n - 1 - j] = f"{k:>{m}}"
            k -= 1

k = 1
for i in range(n // 2):
    for j in range(n // 2):
        if mas[i][j] == f"{k:>{m}}":
            a = i
            b = j
            while mas[i][b + 1] != f"{k:>{m}}":
                mas[i][b] = f"{k:>{m}}"
                b += 1
            mas[i][b] = f"{k:>{m}}"
            while mas[a + 1][j] != f"{k:>{m}}":
                mas[a][j] = f"{k:>{m}}"
                a += 1
            mas[a][j] = f"{k:>{m}}"

            a = i
            b = j
            while mas[n - 1 - i][b + 1] != f"{k:>{m}}":
                mas[n - 1 - i][b] = f"{k:>{m}}"
                b += 1
            mas[n - 1 - i][b] = f"{k:>{m}}"
            while mas[a + 1][n - 1 - j] != f"{k:>{m}}":
                mas[a][n - 1 - j] = f"{k:>{m}}"
                a += 1
            mas[a][n - 1 - j] = f"{k:>{m}}"

            k += 1

for i in range(n):
    print(*mas[i])
