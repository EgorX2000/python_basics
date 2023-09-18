n = int(input())

i = 0
s = 0
flag = False
while i < n:
    if (a := input()) == "ВСЁ":
        i += 1
        flag = False
    if a == "зайка" and not flag:
        s += 1
        flag = True

print(s)
