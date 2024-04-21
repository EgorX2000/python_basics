import requests
import json

server_address = "http://" + input() + "/users"
data = {
    "username": input(),
    "last_name": input(),
    "first_name": input(),
    "email": input()
}

requests.post(server_address, data=json.dumps(data))
