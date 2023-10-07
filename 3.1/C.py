L = int(input())
N = int(input())

for i in range(N):
    article = input()

    if len(article) <= L:
        print(article)
    else:
        print(article[:L - 3], end="...\n")
