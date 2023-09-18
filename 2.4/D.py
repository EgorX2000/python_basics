n = int(input())

s = 0
for i in range(n):
    a = input()
    for c in a:
        s += int(c)

print(s)
