def gcd(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1

    return (n1 + n2)


nums = sorted(list(map(int, input().split())))
answer = gcd(nums[0], nums[1])

for i in range(2, len(nums)):
    answer = gcd(answer, nums[i])

print(answer)
