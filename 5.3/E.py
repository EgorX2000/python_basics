def merge(tup_1, tup_2):
    try:
        check_1 = iter(tup_1)
        check_2 = iter(tup_2)
    except TypeError:
        raise StopIteration
    if not (all(isinstance(i, type(tup_1[0])) for i in tup_1) and all(isinstance(i, type(tup_1[0])) for i in tup_2)):
        raise TypeError
    if list(tup_1) != sorted(tup_1) or list(tup_2) != sorted(tup_2):
        raise ValueError

    ans = list(tup_1) + list(tup_2)
    ans.sort()
    return tuple(ans)
