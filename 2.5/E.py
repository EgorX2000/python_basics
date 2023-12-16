n = int(input())

i = 0
ans = 0
while i < n:
    s = 0
    count = 0
    while (string := input()) != "stop":
        s += int(string)
        count += 1
    else:
        ans += s / count
    i += 1

print(f"{ans:.2f}")
