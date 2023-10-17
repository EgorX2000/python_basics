rle = [('a', 2), ('b', 3), ('c', 1)]

ans = "".join(elem * count for elem, count in rle)

print(ans)
