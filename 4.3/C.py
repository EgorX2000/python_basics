def make_equation(*nums):
    if len(nums) == 1:
        return nums[-1]
    return f"({make_equation(*nums[:-1])}) * x + {nums[-1]}"
