with open(input(), "r") as file:
    data = file.readlines()

count = int(input())
print(*data[-count:], sep="")
