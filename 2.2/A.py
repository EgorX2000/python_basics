username = input("Как Вас зовут?\n")
print(f"Здравствуйте, {username}!")
match input("Как дела?\n").lower():
    case "хорошо":
        print("Я за вас рада!")
    case "плохо":
        print("Всё наладится!")
    case _:
        print("Error")
