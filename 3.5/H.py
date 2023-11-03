words = list()
for i in range(3):
    if i != 2:
        with open(input(), "r") as file:
            for line in file:
                words.extend(line.split())
    else:
        with open(input(), "w") as file:
            for word in sorted(set(words)):
                if words.count(word) == 1:
                    file.write(word + "\n")
