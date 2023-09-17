n = 500
print(n)

more = 1
less = 1001
while (i := input()) != "Угадал!":
    if i == "Больше":
        more = n
        if n + n // 2 <= less:
            n += n // 2
        else:
            n += (less - n) // 2
        print(n)
    elif i == "Меньше":
        less = n
        if n - n // 2 >= more:
            n -= n // 2
        else:
            n -= (n - more) // 2
        print(n)
