n = int(input())

i = 2
mas = list()
while i <= n:
    if n % i == 0:
        n //= i
        mas.append(i)
    else:
        i += 1
else:
    print(*mas, sep=" * ")
