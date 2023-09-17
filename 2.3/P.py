n = input()

if len(n) % 2 == 0:
    if n[0: len(n) // 2] == n[-1: len(n) // 2 - 1: -1]:
        print("YES")
    else:
        print("NO")
else:
    if n[0: len(n) // 2 + 1] == n[-1: len(n) // 2 - 1: -1]:
        print("YES")
    else:
        print("NO")
