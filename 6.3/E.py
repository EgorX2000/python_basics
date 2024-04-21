import requests
import sys

server_address = "http://" + input()

ans = 0
for path in sys.stdin:
    data = requests.get(server_address + path.strip()).json()
    for elem in data:
        if isinstance(elem, int):
            ans += elem

print(ans)
