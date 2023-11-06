import json
import sys

nums = list()
keys = list()
for line in sys.stdin:
    nums.append(int(line.strip()))
    for char in line.strip():
        if char not in keys:
            keys.append(char)

ans = dict()
for key in keys:
    for num in nums:
        if key in str(num):
            if key in ans:
                ans[key].append(num)
                ans[key] = sorted(set(ans[key]))
            else:
                ans[key] = [num]

with open("result.json", "w") as file:
    json.dump(ans, file, indent=4)
