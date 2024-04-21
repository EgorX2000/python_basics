import requests

server_address = "http://" + input() + "/users/" + input()

requests.delete(server_address)
