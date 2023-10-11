n = int(input())

words = set()
for i in range(n):
    for word in input().split():
        words.add(word)

for word in words:
    print(word)
