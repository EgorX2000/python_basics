n = int(input())

flag = True
for i in range(n):
    i = input()
    if not (i[0] in "абв"):
        flag = False

if flag:
    print("YES")
else:
    print("NO")
