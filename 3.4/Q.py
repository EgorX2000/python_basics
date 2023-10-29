import itertools

suits = ["бубен", "пик", "треф", "червей"]
values = ["10", "2", "3", "4", "5", "6", "7",
          "8", "9", "валет", "дама", "король", "туз"]

inc_suit = input()
exc_value = input()
last = input()

preferred_suit = [suit for suit in suits if suit[:3] == inc_suit[:3]][0]
values.remove(exc_value)
combination = list(itertools.permutations(
    itertools.product(sorted(values), sorted(suits)), 3))
variants = sorted(set([", ".join(" ".join(i)
                  for i in sorted(j)) for j in combination]))
answers = [i for i in variants if preferred_suit in i]
for i in range(len(answers)):
    if answers[i] == last:
        print(answers[i + 1])
        break
