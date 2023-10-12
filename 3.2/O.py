numbers = list(map(int, input().split()))

info = list()
for number in numbers:
    number = bin(number).removeprefix("0b")
    info.append({"digits": len(number),
                 "units": number.count("1"),
                 "zeros": number.count("0")})

print(info)
