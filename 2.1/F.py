name = input()
price = int(input())
weight = int(input())
cash = int(input())

change = cash - price * weight
receipt = f"""Чек
{name} - {weight}кг - {price}руб/кг
Итого: {price * weight}руб
Внесено: {cash}руб
Сдача: {change}руб
"""

print(receipt)
