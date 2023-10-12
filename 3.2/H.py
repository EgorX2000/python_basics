n = int(input())

preferences = dict()
for i in range(n):
    info = input().split()
    surname = info[0]
    for porridge in info[1:]:
        if porridge in preferences:
            preferences[porridge].add(surname)
        else:
            preferences[porridge] = {surname}

porridge = input()
if porridge in preferences:
    print(*sorted(preferences[porridge]), sep="\n")
else:
    print("Таких нет")
