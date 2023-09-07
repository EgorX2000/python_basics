name = input()
price = int(input())
weight = int(input())
cash = int(input())

change = cash - price * weight
receipt = f"""{"=" * 16}Чек{"=" * 16}
Товар:{" " * (35 - len("Товар:") - len(name))}{name}
Цена:{" " * (35 - len("Цена:кг * руб/кг") - len(str(weight)) - len(str(price)))}{weight}кг * {price}руб/кг
Итого:{" " * (35 - len("Итого:руб") - len(str(price * weight)))}{price * weight}руб
Внесено:{" " * (35 - len("Внесено:руб") - len(str(cash)))}{cash}руб
Сдача:{" " * (35 - len("Сдача:руб") - len(str(change)))}{change}руб
{"=" * 35}
"""

print(receipt)
