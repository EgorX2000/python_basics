n = int(input())

employees = dict()
for i in range(n):
    surname = input()
    if surname in employees:
        employees[surname] += 1
    else:
        employees[surname] = 1

count = 0
for surname in sorted(employees):
    if employees[surname] > 1:
        count += employees[surname]
        print(surname, employees[surname], sep=" - ")

if count == 0:
    print("Однофамильцев нет")
