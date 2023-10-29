import itertools

suits = ["пик", "треф", "бубен", "червей"]
values = ["2", "3", "4", "5", "6", "7", "8",
          "9", "10", "валет", "дама", "король", "туз"]

suits.remove(input())
print(*[f"{value} {suit}" for value, suit in list(
    itertools.product(values, suits))], sep="\n")
