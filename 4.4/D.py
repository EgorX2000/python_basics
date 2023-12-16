def rindex(text):
    letters = set()
    ans = dict()
    for i in range(len(text) - 1, -1, -1):
        if text[i].isalpha() and text[i] not in letters:
            ans[text[i]] = i
            letters.add(text[i])

    for letter in sorted(ans):
        yield (letter, ans[letter])
