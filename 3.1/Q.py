str_in = input().lower().replace(" ", "")

if len(str_in) % 2 == 0 and str_in[:len(str_in) // 2 - 1] == str_in[:len(str_in) // 2:-1]:
    print("YES")
elif len(str_in) % 2 != 0 and str_in[:len(str_in) // 2] == str_in[:len(str_in) // 2:-1]:
    print("YES")
else:
    print("NO")
