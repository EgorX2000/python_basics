items = list()
for _ in range(int(input())):
    items.extend(input().split(sep=", "))

for index, value in enumerate(sorted(items), 1):
    print(f"{index}. {value}")
