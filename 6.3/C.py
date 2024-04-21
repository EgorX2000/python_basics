import requests

server_address = "http://" + input()

data = requests.get(server_address).json()
ans = 0
for elem in data:
    if isinstance(elem, int):
        ans += elem

print(ans)
