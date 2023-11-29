def recursive_digit_sum(num):
    if len(str(num)) == 1:
        return num
    return int(str(num)[-1]) + recursive_digit_sum(int(str(num)[:-1]))
