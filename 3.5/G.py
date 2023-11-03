data = list()
with open(input(), "r") as file:
    for line in file:
        data.extend([int(num) for num in line.split()])

print(len(data), len([num for num in data if num > 0]), min(
    data), max(data), sum(data), round(sum(data) / len(data), 2), sep="\n")
