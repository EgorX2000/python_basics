n = int(input())
hl = 0
for i in range(n):
    b = int(input())
    if i == 0:
        hl = 0
    else:
        hl = h
    h = b % 256
    b //= 256
    r = b % 256
    m = b // 256
    if h > 100 or h != (37 * (m + r + hl)) % 256:
        print(i)
        break
else:
    print("-1")
