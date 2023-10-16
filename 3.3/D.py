numbers = list(map(int, input().split(sep=", ")))

ans = {elem for elem in numbers if elem % 2 != 0}

print(ans)
