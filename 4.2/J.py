def secret_replace(text, **rules):
    ans = str()
    dicktionary = dict()
    for char in text:
        if char in rules:
            if char not in dicktionary:
                dicktionary[char] = 0
            else:
                dicktionary[char] += 1
            if dicktionary[char] == len(rules[char]):
                dicktionary[char] = 0
            ans += rules[char][dicktionary[char]]
        else:
            ans += char

    return ans
