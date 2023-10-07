letters = dict()

while (str_in := input()) != "ФИНИШ":
    for char in str_in:
        if char != " ":
            char = char.lower()
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

for key in sorted(letters):
    if letters[key] == max(letters.values()):
        print(key)
        break
