n = int(input())

nums = list()
for i in range(n):
    nums.append(int(input()))

p = int(input())
for number in nums:
    print(number ** p)
