a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b != 0:
        print(round(-c / b, 2))
    elif c == 0:
        print("Infinite solutions")
    else:
        print("No solution")
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        print(min(round((-b - d ** 0.5) / (2 * a), 2), round((-b + d ** 0.5) / (2 * a), 2)),
              max(round((-b - d ** 0.5) / (2 * a), 2), round((-b + d ** 0.5) / (2 * a), 2)))
    elif d == 0:
        print(round(-b / (2 * a), 2))
    else:
        print("No solution")
