class Rectangle:
    def __init__(self, point_1, point_2):
        self.left = min(point_1[0], point_2[0])
        self.top = max(point_1[1], point_2[1])
        self.right = max(point_1[0], point_2[0])
        self.bottom = min(point_1[1], point_2[1])
        self.w = round(abs(point_1[0] - point_2[0]), 2)
        self.h = round(abs(point_1[1] - point_2[1]), 2)
        self.x = min(point_1[0], point_2[0])
        self.y = max(point_1[1], point_2[1])
        self.flag = False

    def perimeter(self):
        return round(abs(self.left - self.right) * 2 + abs(self.top - self.bottom) * 2, 2)

    def area(self):
        return round(abs(self.left - self.right) * abs(self.top - self.bottom), 2)

    def get_pos(self):
        return self.left, self.top

    def get_size(self):
        if self.flag:
            return self.w, self.h
        return ((round(abs(self.left - self.right), 2), round(abs(self.top - self.bottom), 2)))

    def resize(self, width, height):
        self.flag = False
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top + height, 2)
        self.w, self.h = width, height

    def turn(self):
        self.flag = False
        width, height = self.get_size()
        d = (width - height) / 2
        self.left = round(self.left + d, 2)
        self.right = round(self.right - d, 2)
        self.top = round(self.top + d, 2)
        self.bottom = round(self.bottom - d, 2)
        d = (self.w - self.h) / 2
        self.x = round(self.x + d, 2)
        self.y = round(self.y + d, 2)
        self.w, self.h = self.h, self.w

    def scale(self, factor):
        self.flag = False
        width, height = self.get_size()
        self.flag = False
        if abs(width - self.w) <= 0.01:
            width = self.w
        if abs(height - self.h) <= 0.02:
            height = self.h
        self.left = round(self.left - (factor * width - width) / 2, 2)
        self.top = round(self.top + (factor * height - height) / 2, 2)
        width = round(width * factor, 2)
        height = round(height * factor, 2)
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top - height, 2)
        self.x = round(self.x - (factor * self.w - self.w) / 2, 2)
        self.y = round(self.y + (factor * self.h - self.h) / 2, 2)
        self.w = round(self.w * factor, 2)
        self.h = round(self.h * factor, 2)
