def s(num, base):
    new = str()

    while num > 0:
        new = str(num % base) + new
        num //= base

    s = 0
    for c in new:
        s += int(c)

    return s


n = int(input())
ms = 0
for i in range(2, 10 + 1):
    ms = max(ms, s(n, i))

for i in range(2, 10 + 1):
    if s(n, i) == ms:
        print(i)
        break
