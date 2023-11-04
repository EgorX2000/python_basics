file_in = input()
first = input()
second = input()
third = input()
with open(file_in, "r") as file_in:
    with open(first, "a") as first:
        with open(second, "a") as second:
            with open(third, "a") as third:
                for line in file_in:
                    even = list()
                    odd = list()
                    eq = list()

                    line = line.split()
                    for num in line:
                        ch = nch = 0
                        for char in num:
                            if char in "02468":
                                ch += 1
                            else:
                                nch += 1
                        if ch > nch:
                            even.append(num)
                        elif ch < nch:
                            odd.append(num)
                        else:
                            eq.append(num)

                    print(*even, file=first)
                    print(*odd, file=second)
                    print(*eq, file=third)
