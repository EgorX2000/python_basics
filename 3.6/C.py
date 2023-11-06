ints = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
ans = [num for num in ints if int(
    str(num)[-1]) > 3] + [num for num in ints if int(str(num)[-1]) <= 3]
print(ans)
