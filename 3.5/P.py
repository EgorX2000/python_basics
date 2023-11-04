import sys

search = input().lower()
files = list()
for line in sys.stdin:
    files.append(line.strip())

count = 0
for file in files:
    data = str()
    with open(file, "r", encoding="UTF-8") as opened:
        for line in opened:
            if len(line) > 1:
                line = line.replace("\n", " ")
                while "  " in line:
                    line = line.replace("  ", " ")
                data += line.lower()
    if search in data:
        print(file)
        count += 1

if count == 0:
    print("404. Not Found")
