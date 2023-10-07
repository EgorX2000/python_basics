import math

stack = list(input().split())

index = 0
while len(stack) > 1:
    if not (stack[index].isdigit()):
        if stack[index] in "+-*/":
            if stack[index] == "/":
                stack[index - 2] = str(eval("//".join(stack[index - 2:index])))
            else:
                stack[index -
                      2] = str(eval(stack[index].join(stack[index - 2:index])))
            del stack[index - 1:index + 1]
            index -= 2
        elif stack[index] in "~!#":
            if stack[index] == "~":
                stack[index - 1] = "-" + stack[index - 1]
                del stack[index]
                index -= 1
            elif stack[index] == "!":
                stack[index - 1] = str(math.factorial(int(stack[index - 1])))
                del stack[index]
                index -= 1
            else:
                stack[index] = stack[index - 1]
        else:
            stack[index - 3:index] = stack[index -
                                           2], stack[index - 1], stack[index - 3]
            del stack[index]
            index -= 1
    index += 1
else:
    print(*stack)
