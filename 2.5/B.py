a = int(input())
b = int(input())
string = input()

if len(string) % 6 == 0:
    print(a + b)
elif len(string) % 3 == 0:
    print(a - b)
elif len(string) % 2 == 0:
    print(a * b)
else:
    print(a // b)
