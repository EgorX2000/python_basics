a = int(input())
b = int(input())

m = len(str(a * b))

for i in range(1, a + 1):
    k = i
    for j in range(b):
        print(f"{k:>{m}}", end=" ")
        k += a
    print()
