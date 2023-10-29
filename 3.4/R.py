expression = input()
print("a b c f")
for i in range(8):
    values = list(bin(i)[2:].zfill(3))
    a, b, c = map(int, values)
    print(" ".join(values), int(eval(expression)))
