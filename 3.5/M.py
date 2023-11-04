import json
import sys

name = input()
updates = [line.strip() for line in sys.stdin]
with open(name, "r", encoding="UTF-8") as file:
    data = json.load(file)

dicktionary = {line.split(" == ")[0]: line.split(" == ")[
    1] for line in updates}
data.update(dicktionary)

with open(name, "w", encoding="UTF-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)
