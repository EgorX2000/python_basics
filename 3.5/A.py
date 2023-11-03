import sys

ans = 0
for line in sys.stdin:
    ans += sum(list(map(int, line.split())))

print(ans)
