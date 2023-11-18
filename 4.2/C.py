def gcd(*nums):
    values = list(nums)

    while len(values) > 1:
        n1 = values[0]
        n2 = values[1]

        while n1 != 0 and n2 != 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1

        del values[0]
        values[0] = n1 + n2
    else:
        return values[0]
