n = int(input())
for _ in range(n):
    str_in = input().split(sep="%")
    a, s, b = int(str_in[0]), str_in[1], int(str_in[2])
    ans = ""
    for i in range(b):
        if a <= len(s):
            ind = a - i * 3
        else:
            ind = -i * 3
        if ind >= 0:
            ans = s[ind] + ans
    print(ans)
