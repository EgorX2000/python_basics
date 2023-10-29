import itertools

n = int(input())
nums = [i + 1 for i in range(n)]
nums = list(itertools.product(nums, nums))

for i in range(n ** 2):
    print(nums[i][0] * nums[i][1], end=" ")
    if (i + 1) % n == 0:
        print()
