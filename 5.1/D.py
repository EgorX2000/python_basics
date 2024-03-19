class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.time = 0
        if position == "Junior":
            self.position = 1
            self.salary = 10
        elif position == "Middle":
            self.position = 2
            self.salary = 15
        else:
            self.position = 3
            self.salary = 20
        self.money = 0

    def work(self, time):
        self.time += time
        self.money += time * self.salary

    def rise(self):
        self.position += 1
        if self.position <= 3:
            self.salary += 5
        else:
            self.salary += 1

    def info(self):
        return f"{self.name} {self.time}ч. {self.money}тгр."
