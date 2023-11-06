import sys

catalog = dict()
for line in sys.stdin:
    line = line.upper().split()
    for word in line:
        if len(word) in catalog:
            catalog[len(word)].append(word)
        else:
            catalog[len(word)] = [word]

for key in catalog:
    catalog[key] = sorted(set(catalog[key]))
    catalog[key].sort(reverse=True)
    data = str(catalog[key]).removeprefix(
        "[").removesuffix("]").replace("'", "").replace(",", ";")
    print(f"{key}: {data}")
