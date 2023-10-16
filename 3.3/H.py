string = input()

ans = ''.join(word[0] for word in string.split()).upper()

print(ans)
