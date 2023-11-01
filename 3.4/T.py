def sub(expression):
    global values

    args = sorted(set([char for char in expression if char.isupper()]))
    args.extend(["0", "1"])

    if len(expression) == 1:
        return values[expression]

    if "not" in expression:
        for i in range(len(args)):
            expression = expression.replace(
                f"not {args[i]}", str(eval(f"not {values[args[i]]}")))

    while "and" in expression:
        for i in range(len(args)):
            for j in range(len(args)):
                expression = expression.replace(f"{args[i]} and {args[j]}", str(eval(
                    f"{values[args[i]]} and {values[args[j]]}"))).replace("False", "0").replace("True", "1")

    while "or" in expression:
        for i in range(len(args)):
            for j in range(len(args)):
                expression = expression.replace(f"{args[i]} or {args[j]}", str(eval(
                    f"{values[args[i]]} or {values[args[j]]}"))).replace("False", "0").replace("True", "1")

    while "^" in expression:
        for i in range(len(args)):
            for j in range(len(args)):
                expression = expression.replace(f"{args[i]} ^ {args[j]}", str(eval(
                    f"{values[args[i]]} != {values[args[j]]}"))).replace("False", "0").replace("True", "1")

    while "->" in expression:
        for i in range(len(args)):
            for j in range(len(args)):
                expression = expression.replace(f"{args[i]} -> {args[j]}", str(eval(
                    f"{values[args[i]]} <= {values[args[j]]}"))).replace("False", "0").replace("True", "1")

    while "~" in expression:
        for i in range(len(args)):
            for j in range(len(args)):
                expression = expression.replace(f"{args[i]} ~ {args[j]}", str(eval(
                    f"{values[args[i]]} == {values[args[j]]}"))).replace("False", "0").replace("True", "1")

    return expression


expression = input()
args = sorted(set([char for char in expression if char.isupper()]))

print(" ".join(args) + " F")
args.extend(["0", "1"])
for i in range(2 ** (len(args) - 2)):
    values = dict()
    for j in range((len(args) - 2)):
        values[args[j]] = bin(i)[2:].zfill((len(args) - 2))[j]
    values["0"] = "0"
    values["1"] = "1"

    ans = expression
    while "(" in ans:
        ans = ans.replace(ans[ans.rindex("("):ans.index(
            ")") + 1], sub(ans[ans.rindex("(") + 1:ans.index(")")]))

    print(" ".join(list(values.values())[:-2]), int(sub(ans)))
