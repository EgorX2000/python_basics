n1 = sorted(input())
n2 = sorted(input())

print(max(n1[1], n2[1]), (int(min(n1[1], n2[1])) +
      int(max(n1[0], n2[0]))) % 10, min(n1[0], n2[0]), sep="")
