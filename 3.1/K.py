n = int(input())
strings = list()

for i in range(n):
    strings.append(input())

target = input().lower()

for string in strings:
    if target in string.lower():
        print(string)
