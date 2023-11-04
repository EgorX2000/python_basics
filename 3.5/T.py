with open("numbers.num", "rb") as file:
    data = file.read()

print(sum([int.from_bytes(data[num:num + 2], "big")
      for num in range(0, len(data), 2)]) % 2 ** 16)
