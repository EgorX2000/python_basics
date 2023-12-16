import itertools


def multiple_sum(*numbers, div=2):
    s = sum(numbers)
    if s % div == 0:
        return s
    else:
        ans = list()
        for r in range(1, len(numbers) + 1):
            r = list(itertools.chain(
                itertools.combinations(numbers, r)))
            for elem in r:
                if sum(elem) % div == 0:
                    ans.append(sum(elem))
        return max(ans)
