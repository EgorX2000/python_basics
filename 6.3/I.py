import requests
import json
import sys

server_address = "http://" + input() + "/users/" + input()


data = dict()
for string in sys.stdin:
    key, value = string.strip().split(sep="=")
    data[key] = value


requests.put(server_address, data=json.dumps(data))
