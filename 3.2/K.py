n = int(input())

employees = dict()
for i in range(n):
    surname = input()
    if surname in employees:
        employees[surname] += 1
    else:
        employees[surname] = 1

count = 0
for surname in employees:
    if employees[surname] > 1:
        count += employees[surname]

print(count)
