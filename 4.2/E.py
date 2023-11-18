def to_string(*data, sep=" ", end="\n"):
    ans = str()
    for item in data:
        ans += str(item) + sep

    return ans[:-len(sep)] + end
