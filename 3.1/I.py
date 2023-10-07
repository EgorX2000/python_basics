while len(str_in := input()) != 0:
    index = str_in.find("#")
    if index == -1:
        print(str_in)
    elif index > 0:
        print(str_in[:index])
