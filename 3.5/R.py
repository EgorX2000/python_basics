import os

size = os.path.getsize(input())
b = size
kb = b / 1024
mb = kb / 1024
gb = mb / 1024

if gb > 1:
    print(str(int(gb) + 1) + "ГБ")
elif mb > 1:
    print(str(int(mb) + 1) + "МБ")
elif kb > 1:
    print(str(int(kb) + 1) + "КБ")
else:
    print(str(b) + "Б")
