print(*filter(lambda num: sum(map(int, [*str(num)])) % 2 == 0, (1, 2, 3)))
