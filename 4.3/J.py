def make_linear(mas):
    ans = list()
    for elem in mas:
        if type(elem) is list:
            ans.extend(make_linear(elem))
        else:
            ans.append(elem)
    return ans
