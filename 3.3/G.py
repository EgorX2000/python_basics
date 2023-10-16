numbers = list(map(int, input().split(sep=", ")))

ans = {number: sorted(list(set(i for i in range(
    1, number + 1) if number % i == 0))) for number in numbers}

print(ans)
