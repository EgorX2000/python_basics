import json


def add(users):
    for user in users:
        if user["name"] not in data:
            data[user["name"]] = dict()
        for info in user:
            if info != "name":
                if info in data[user["name"]]:
                    if user[info] > data[user["name"]][info]:
                        data[user["name"]][info] = user[info]
                else:
                    data[user["name"]][info] = user[info]


data = dict()
with open(name := input(), "r") as file:
    users = json.load(file)

with open(input(), "r") as file:
    updates = json.load(file)

add(users)
add(updates)

with open(name, "w") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
    print(json.load(file))
