a = n1 = int(input())
b = n2 = int(input())

while n1 != 0 and n2 != 0:
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1

print(a * b // (n1 + n2))
