str_in = input()

last = str_in[0]
count = 1
for i in range(1, len(str_in)):
    if str_in[i] != last:
        print(last, count)
        last = str_in[i]
        count = 1
    else:
        count += 1

print(last, count)
