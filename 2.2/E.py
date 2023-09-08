n = int(input())
m = int(input())

p = 7
v = 6

p -= 3
v += 3
p += 2
v += 5 - 2
p += n
v += m

print("Петя" if p > v else "Вася")
