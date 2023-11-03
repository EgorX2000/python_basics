import sys

words = set()
for line in sys.stdin:
    for word in line.split():
        if word.lower() == word.lower()[::-1]:
            words.add(word)

print(*sorted(words), sep="\n")
