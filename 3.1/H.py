n = int(input())

for i in range(n):
    str_in = input()
    if "зайка" in str_in:
        count = 1
        for word in str_in.split():
            if word == "зайка":
                print(count)
                break
            else:
                count += len(word) + 1
    else:
        print("Заек нет =(")
