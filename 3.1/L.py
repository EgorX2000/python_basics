timetable = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

n = int(input())
day = 0
for i in range(n):
    print(timetable[day])
    day += 1
    if day == len(timetable):
        day = 0
