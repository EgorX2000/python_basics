print(str(list(zip(input().split(sep=", "), input().split(sep=", ")))).removeprefix("[").removesuffix(
    "]").replace("), (", "\n").replace("(", "").replace(")", "").replace("'", "").replace(", ", " - "))
