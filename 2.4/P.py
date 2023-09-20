size = int(input())
width = int(input())

length = (width * size) + (size - 1)
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{(i * j):^{width}}", end="")
        if j != size:
            print("|", end="")
    if i != size:
        print("\n" + "-" * length)
