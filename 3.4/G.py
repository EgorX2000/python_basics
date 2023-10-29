import itertools

print(*[f"{player_1} - {player_2}" for player_1, player_2 in list(
    itertools.combinations([input() for _ in range(int(input()))], 2))], sep="\n")
