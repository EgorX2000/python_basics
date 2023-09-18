n = int(input())

ms = 0
mname = str()
for i in range(n):
    name = input()
    num = input()
    s = 0
    for c in num:
        s += int(c)
    if s >= ms:
        ms = s
        mname = name

print(mname)
