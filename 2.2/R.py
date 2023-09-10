a = int(input())
b = int(input())
c = int(input())

sides = sorted([a, b, c])
cos = (sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) / \
    (2 * sides[0] * sides[1])
if cos > 0:
    print("крайне мала")
elif cos < 0:
    print("велика")
else:
    print("100%")
