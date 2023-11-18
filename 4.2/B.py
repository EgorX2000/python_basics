def make_matrix(size, value=0):
    if type(size) is int:
        return [[value] * size for _ in range(size)]
    else:
        return [[value] * size[0] for _ in range(size[1])]
