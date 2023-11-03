import sys

ans = 0
count = 0
for line in sys.stdin:
    line = line.split()
    ans += int(line[2]) - int(line[1])
    count += 1

print(round(ans / count))
