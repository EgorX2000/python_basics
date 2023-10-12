friends = dict()
while len(str_in := input().split()) > 0:
    if str_in[0] in friends:
        friends[str_in[0]].add(str_in[1])
    else:
        friends[str_in[0]] = {str_in[1]}

    if str_in[1] in friends:
        friends[str_in[1]].add(str_in[0])
    else:
        friends[str_in[1]] = {str_in[0]}

for man_1 in friends:
    print(man_1, end=": ")
    for man_2 in friends:
        if man_1 in friends[man_2]:
            print(man_2, end=" ")
