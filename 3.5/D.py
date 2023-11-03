import sys

data = list()
for line in sys.stdin:
    data.append(line)

search = data[-1][:-1].lower()
data.pop()
print(*[line for line in data if search in line.lower()], sep="")
