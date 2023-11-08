def merge(tup_1, tup_2):
    merged = list(tup_1) + list(tup_2)

    for i in range(len(merged) - 1):
        for j in range(len(merged) - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]

    return tuple(merged)
