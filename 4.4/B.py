def add_word(word):
    words.append(word)


def get_work():
    return str(words).removeprefix("[").removesuffix("]").replace("'", "") + ". " + f"({len(words)})"


words = list()
