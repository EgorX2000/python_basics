import json
import sys

answers = list()
for ans in sys.stdin:
    answers.append(ans.strip())

correct = list()
with open("scoring.json", "r") as file:
    data = json.load(file)

i = 0
score = 0
for group in data:
    weight = int(group["points"]) // len(group["tests"])
    for test in group["tests"]:
        if test["pattern"] == answers[i]:
            score += weight
        i += 1

print(score)
