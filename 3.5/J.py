with open(input(), "r") as file:
    data = file.readlines()

formatted = list()
for line in data:
    if len(line) > 1:
        line = line.replace("\t", "")
        while line[0] == " ":
            line = line[1:]
        while line[-1] == " ":
            line = line[:-1]
        while "  " in line:
            line = line.replace("  ", " ")
        formatted.append(line)

with open(input(), "w") as file:
    file.writelines(formatted)
