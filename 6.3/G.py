import requests
import sys

server_address = "http://" + input() + "/users/" + input()
message = "".join(i for i in sys.stdin)

data = {}

try:
    data = requests.get(server_address).json()
except ValueError:
    print("Пользователь не найден")

if data:
    for key in data:
        message = message.replace("{" + key + "}", str(data[key]))
    print(message)
