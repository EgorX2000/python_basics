import requests

server_address = "http://" + input() + "/users"

data = requests.get(server_address).json()

names = []
for elem in data:
    names.append(f"{elem['last_name']} {elem['first_name']}")

for name in sorted(names):
    print(name)
