import itertools

params = list(map(float, input().split()))
for value in itertools.count(params[0], params[2]):
    if value <= params[1]:
        print(f"{value:.2f}")
    else:
        break
