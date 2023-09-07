n1 = f"{input():0>3}"
n2 = f"{input():0>3}"

print(str((int(n1[0]) + int(n2[0])) % 10) + str((int(n1[1]) +
      int(n2[1])) % 10) + str((int(n1[2]) + int(n2[2])) % 10))
