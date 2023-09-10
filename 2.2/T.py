s1 = input()
s2 = input()
s3 = input()

strings = sorted([s1, s2, s3])
for s in strings:
    if "зайка" in s:
        print(s, len(s))
        break
