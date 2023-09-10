x = float(input())
y = float(input())

r = (x ** 2 + y ** 2) ** 0.5
if r > 10:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
else:
    # 1st quarter
    if x >= 0 and y >= 0:
        if r > 5:
            print("Зона безопасна. Продолжайте работу.")
        else:
            print("Опасность! Покиньте зону как можно скорее!")

    # 2nd quarter
    if x < 0 and y >= 0:
        # rectangle
        if -4 <= x < 0:
            if y > 5:
                print("Зона безопасна. Продолжайте работу.")
            else:
                print("Опасность! Покиньте зону как можно скорее!")
        else:
            if y > (5 / 3) * x + (35 / 3):
                print("Зона безопасна. Продолжайте работу.")
            else:
                print("Опасность! Покиньте зону как можно скорее!")

    # 3&4 quarters
    if y < 0:
        if y <= 0.25 * x ** 2 + 0.5 * x - 8.75:
            print("Зона безопасна. Продолжайте работу.")
        else:
            print("Опасность! Покиньте зону как можно скорее!")
