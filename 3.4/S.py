expression = input()
args = sorted(set([char for char in expression if char.isupper()]))
print(" ".join(args) + " F")
for i in range(2 ** len(args)):
    values = list(bin(i)[2:].zfill(len(args)))
    exec(", ".join(args) + " = map(int, values)")
    print(" ".join(values), int(eval(expression)))
