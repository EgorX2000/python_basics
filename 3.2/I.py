data = dict()
while len(str_in := input()) > 0:
    str_in = str_in.split()
    for word in str_in:
        if word in data:
            data[word] += 1
        else:
            data[word] = 1

for word in data:
    print(word, data[word])
