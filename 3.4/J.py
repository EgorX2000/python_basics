n = int(input())
print("А Б В")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        k = n - i - j
        if i > 0 and j > 0 and k > 0:
            print(i, j, k)
