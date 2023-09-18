def nod(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    return n1 + n2


n = int(input())

mas = list()
for i in range(n):
    mas.append(int(input()))


mas.sort()
nd = mas[0]
for i in range(1, len(mas)):
    nd = nod(nd, mas[i])

print(nd)
