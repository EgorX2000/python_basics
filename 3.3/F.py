text = input()

ans = {letter: text.lower().count(letter)
       for letter in text.lower() if letter.isalpha()}

print(ans)
