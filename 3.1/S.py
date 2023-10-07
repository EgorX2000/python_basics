stack = list(input().split())

index = 0
while len(stack) > 1:
    if not (stack[index].isdigit()):
        stack[index - 2] = str(eval(stack[index].join(stack[index - 2:index])))
        del stack[index - 1:index + 1]
        index -= 2
    index += 1
else:
    print(*stack)
