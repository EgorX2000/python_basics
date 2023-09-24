n = int(input())
n1 = n

length = 1
k = 1
while n1 > 0:
    for i in range(min(length, n1)):
        print(k, end=" ")
        k += 1
    print()

    n1 -= length
    length += 1
