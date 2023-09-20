n = int(input())

print("А Б В")
for a in range(1, n - 1):
    for b in range(1, n - 1):
        for v in range(1, n - 1):
            if a + b + v == n:
                print(a, b, v)
