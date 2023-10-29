import itertools

string = input().split()
for value in itertools.accumulate(list(elem + " " for elem in string)):
    print(value)
