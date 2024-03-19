class Rectangle:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def perimeter(self):
        return round(abs(self.point_2[0] - self.point_1[0]) * 2 + abs(self.point_2[1] - self.point_1[1]) * 2, 2)

    def area(self):
        return round(abs((self.point_2[0] - self.point_1[0]) * (self.point_2[1] - self.point_1[1])), 2)

    def get_pos(self):
        return round(min(self.point_1[0], self.point_2[0]), 2), round(max(self.point_1[1], self.point_2[1]), 2)

    def get_size(self):
        return round(abs(self.point_2[0] - self.point_1[0]), 2), round(abs(self.point_2[1] - self.point_1[1]), 2)

    def move(self, dx, dy):
        self.point_1 = (self.point_1[0] + dx, self.point_1[1] + dy)
        self.point_2 = (self.point_2[0] + dx, self.point_2[1] + dy)

    def resize(self, width, height):
        self.point_1 = min(self.point_1[0], self.point_2[0]), max(
            self.point_1[1], self.point_2[1])
        self.point_2 = self.point_1[0] + width, self.point_1[1] - height
