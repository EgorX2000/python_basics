n = int(input())

for i in range(n):
    if i == 0:
        s = input()
    else:
        s = min(s, input())

print(s)
