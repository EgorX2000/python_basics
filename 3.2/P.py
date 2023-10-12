objects = set()

while len(str_in := input().split()) > 0:
    for i in range(len(str_in)):
        if str_in[i] == "зайка":
            if i == 0:
                objects.add(str_in[i + 1])
            elif i == len(str_in) - 1:
                objects.add(str_in[i - 1])
            else:
                objects.update({str_in[i - 1], str_in[i + 1]})

print(*objects, sep="\n")
