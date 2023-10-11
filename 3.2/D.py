n = int(input())
m = int(input())

man = set()
for i in range(n):
    man.add(input())

ovs = set()
for i in range(m):
    ovs.add(input())

if (number := len(man & ovs)) > 0:
    print(number)
else:
    print("Таких нет")
