def merge_sort(mas):
    if len(mas) <= 1:
        return mas
    else:
        left = merge_sort(mas[:int(len(mas) / 2)])
        right = merge_sort(mas[int(len(mas) / 2):])
        return merge(left, right)


def merge(left, right):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    else:
        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)

    return result
