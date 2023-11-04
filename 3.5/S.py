shift = int(input())
data = list()
with open("public.txt", "r") as file:
    data = file.readlines()

letters = "abcdefghijklmnopqrstuvwxyz"
with open("private.txt", "w") as file:
    for line in data:
        for char in line:
            if char.lower() in letters:
                print(letters[(letters.find(char.lower()) + shift) %
                      len(letters)] if char.islower() else letters[(letters.find(char.lower()) + shift) %
                      len(letters)].upper(), end="", file=file)
            else:
                print(char, end="", file=file)
