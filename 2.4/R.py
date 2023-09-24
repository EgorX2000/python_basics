n = int(input())
n1 = n

length = 1
k = 1
cur_l = 0
cnt = 0
mas = list()
while n1 > 0:
    for i in range(min(length, n1)):
        cur_l += len(str(k)) + 1
        cnt += 1
        k += 1

    cur_l -= 1
    mas.append([cur_l, cnt])
    cur_l = 0
    cnt = 0

    n1 -= length
    length += 1

k = 1
for c in mas:
    if c[0] != mas[-1][0]:
        print(" " * ((mas[-1][0] - c[0]) // 2), end="")
    for i in range(c[1]):
        print(k, end=" ")
        k += 1
    if c[0] != mas[-1][0]:
        print(" " * ((mas[-1][0] - c[0]) // 2 - 1))
    else:
        print()
