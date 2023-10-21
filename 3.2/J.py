letters = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i", "й": "i",
           "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
           "ф": "f", "х": "kh", "ц": "tc", "ч": "ch", "ш": "sh", "щ": "shch", "ы": "y", "э": "e", "ю": "iu", "я": "ia",
           "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "Zh", "З": "Z", "И": "I", "Й": "I",
           "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U",
           "Ф": "F", "Х": "Kh", "Ц": "Tc", "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ы": "Y", "Э": "E", "Ю": "Iu", "Я": "Ia"}

str_in = input().replace("ё", "е").replace("й", "и").replace("ъ", "").replace(
    "ь", "").replace("Ё", "Е").replace("Й", "И").replace("Ъ", "").replace("Ь", "")

for char in str_in:
    if char in letters:
        print(letters[char], end="")
    else:
        print(char, end="")