s = {"СЕВЕР", "ЮГ", "ЗАПАД", "ВОСТОК"}
x = 0
y = 0
d = str()

while (i := input()) != "СТОП":
    if i in s:
        d = i
    else:
        if d == "СЕВЕР":
            y += int(i)
        if d == "ЮГ":
            y -= int(i)
        if d == "ЗАПАД":
            x -= int(i)
        if d == "ВОСТОК":
            x += int(i)

print(y, x, sep="\n")
