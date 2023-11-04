words = [set(), set()]
for i in range(2):
    with open(input(), "r") as file:
        for line in file:
            words[i].update({word for word in line.split()})

with open(input(), "w") as file:
    for word in sorted(words[0] ^ words[1]):
        file.write(word + "\n")
