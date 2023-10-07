L = int(input())
N = int(input())

remaining = L
for i in range(N):
    str_in = input()

    if len(str_in) < remaining - 3:
        print(str_in)
    else:
        print(str_in[:remaining - 3], end="...\n")
        break

    remaining -= len(str_in)
