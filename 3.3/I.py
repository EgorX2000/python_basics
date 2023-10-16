numbers = list(map(int, input().split(sep=", ")))

ans = " - ".join(str(elem) for elem in sorted(list(set(numbers))))

print(ans)
