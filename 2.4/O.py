a = int(input())
b = int(input())

m = len(str(a * b))

mas = [0] * b
for i in range(b):
    mas[i] = [0] * a

k = 1
for i in range(b):
    if i % 2 == 0:
        for j in range(a):
            mas[i][j] = k
            k += 1
    else:
        for j in range(a - 1, -1, -1):
            mas[i][j] = k
            k += 1

for j in range(a):
    for i in range(b):
        print(f"{mas[i][j]:>{m}}", end=" ")
    print()
