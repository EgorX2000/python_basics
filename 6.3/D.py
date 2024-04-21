import requests

server_address = "http://" + input()
key = input()

data = requests.get(server_address).json()
try:
    print(data[key])
except KeyError:
    print("No data")
