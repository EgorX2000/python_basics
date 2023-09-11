start = int(input())
end = int(input())

if start < end:
    for i in range(start, end + 1):
        print(i, end=" ")
else:
    for i in range(start, end - 1, -1):
        print(i, end=" ")
