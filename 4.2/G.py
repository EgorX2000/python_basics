def enter_results(*nums):
    ch.extend(nums[1::2])
    nch.extend(nums[::2])


def get_sum():
    return (sum(nch), sum(ch))


def get_average():
    return (sum(nch) / len(nch), sum(ch) / len(ch))


ch = list()
nch = list()
