data = list()
for i in range(3):
    data.extend(input().split(sep=", "))

for index, value in enumerate(sorted(data), 1):
    print(f"{index}. {value}")
