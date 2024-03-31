def only_positive_even_sum(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    if not ((a > 0 and a % 2 == 0) and (b > 0 and b % 2 == 0)):
        raise ValueError
    return a + b
