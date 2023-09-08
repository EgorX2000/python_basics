num = input()

s1 = int(num[1]) + int(num[2])
s2 = int(num[0]) + int(num[1])

print(max(s1, s2), min(s1, s2), sep="")
