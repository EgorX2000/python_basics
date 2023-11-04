import json

data = list()
with open(input(), "r") as file:
    for line in file:
        data.extend([int(num) for num in line.split()])

data = {
    "count": len(data),
    "positive_count": len([num for num in data if num > 0]),
    "min": min(data),
    "max": max(data),
    "sum": sum(data),
    "average": round(sum(data) / len(data), 2)
}

with open(input(), "w") as file:
    json.dump(data, file, indent=4)
