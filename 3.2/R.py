n = int(input())

counts = dict()
for i in range(n):
    coords = input().split()
    point = f"{coords[0][:-1]}-{coords[1][:-1]}"
    if point in counts:
        counts[point] += 1
    else:
        counts[point] = 1

print(max(counts.values()))
