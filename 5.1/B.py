class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, point):
        return round((abs(self.x - point.x) ** 2 + abs(self.y - point.y) ** 2) ** 0.5, 2)
