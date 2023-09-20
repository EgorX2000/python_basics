a = int(input())
b = int(input())

m = len(str(a * b))

for i in range(1, a + 1):
    if i % 2 != 0:
        for j in range(1, b + 1):
            print(f"{j + b * (i - 1):>{m}}", end=" ")
    else:
        for j in range(b, 0, -1):
            print(f"{j + b * (i - 1):>{m}}", end=" ")
    print()
