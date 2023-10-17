n = int(input())

toys = set()
children = dict()
for i in range(n):
    data = input().replace(":", "").replace(",", "").split()
    children[data[0]] = set(data[1:])
    toys.update(data[1:])

toys = sorted(list(toys))
for toy in toys:
    count = 0
    for child in children:
        if toy in children[child]:
            count += 1
    if count == 1:
        print(toy)
