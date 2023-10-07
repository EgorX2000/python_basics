n = int(input())

count = 0
for i in range(n):
    count += input().count("зайка")

print(count)
