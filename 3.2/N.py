n = int(input())

products = set()
for i in range(n):
    products.add(input())

m = int(input())
recipes = dict()
for i in range(m):
    recipes[recipe := input()] = set()
    number = int(input())
    for j in range(number):
        recipes[recipe].add(input())

count = 0
for recipe in sorted(recipes):
    if len(recipes[recipe] & products) == len(recipes[recipe]):
        print(recipe)
        count += 1

if count == 0:
    print("Готовить нечего")
