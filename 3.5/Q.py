with open("secret.txt", "r", encoding="UTF-8") as file:
    data = file.readlines()

for line in data:
    for char in line:
        print(chr(ord(char) % 128), end="")
