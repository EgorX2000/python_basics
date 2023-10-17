friends = {}
while man := input().split():
    if man[0] not in friends:
        friends[man[0]] = {man[1]}
    else:
        friends[man[0]].add(man[1])
    if man[1] not in friends:
        friends[man[1]] = {man[0]}
    else:
        friends[man[1]].add(man[0])

friends_2lvl = dict.fromkeys(friends, set())
for man in friends:
    for friend in friends[man]:
        friends_2lvl[man] = friends_2lvl[man] | friends[friend]
    friends_2lvl[man].discard(man)
    for friend in friends[man]:
        friends_2lvl[man].discard(friend)

for man in sorted(friends_2lvl):
    print(f"{man}: {', '.join(sorted(friends_2lvl[man]))}")
