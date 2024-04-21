import requests

server_address = "http://" + input()

ans = 0
while num := int(requests.get(server_address).text):
    ans += num

print(ans)
