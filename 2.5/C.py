n = int(input())
m = int(input())

for i in range(n, m - 1, -((n - m) // 3)):
    if i - (n - m) // 3 >= m:
        print(i, end="; ")
    else:
        print(i)

print("Старт!")
