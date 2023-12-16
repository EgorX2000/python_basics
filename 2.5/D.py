n = int(input())
mas = [int(input()) for _ in range(n)]

ans = 10 ** 100
for i in range(len(mas) - 1):
    if mas[i + 1] > mas[i]:
        ans = min(ans, mas[i + 1])

print(ans)
