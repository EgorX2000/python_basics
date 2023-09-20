a = int(input())
b = int(input())

m = len(str(a * b))

for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(f"{j + b * (i - 1):>{m}}", end=" ")
    print()
