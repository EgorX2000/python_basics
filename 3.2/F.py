n = int(input())
m = int(input())

children = dict()
for i in range(n + m):
    surname = input()
    if surname in children:
        children[surname] += 1
    else:
        children[surname] = 1

if min(children.values()) == 1:
    for surname in sorted(children):
        if children[surname] == 1:
            print(surname)
else:
    print("Таких нет")
