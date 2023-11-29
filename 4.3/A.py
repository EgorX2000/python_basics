def recursive_sum(*nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + recursive_sum(*nums[:-1])
