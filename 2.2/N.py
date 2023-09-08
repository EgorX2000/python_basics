num = sorted(input())

if num[0] != "0":
    print(num[0] + num[1], num[2] + num[1])
elif num[1] != "0":
    print(num[1] + num[0], num[2] + num[1])
else:
    print(num[1] + num[2], num[2] + num[1])
