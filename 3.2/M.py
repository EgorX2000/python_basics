n = int(input())

dishes = set()
for i in range(n):
    dishes.add(input())

m = int(input())
cooked = set()
for i in range(m):
    for j in range(int(input())):
        cooked.add(input())

if len(dishes - cooked) > 0:
    print(*sorted(dishes - cooked), sep="\n")
else:
    print("Готовить нечего")
