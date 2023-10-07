while len(str_in := input()) > 0:
    if str_in[-3:] == "@@@":
        continue
    elif str_in[:2] == "##":
        print(str_in[2:])
    else:
        print(str_in)
