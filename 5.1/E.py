class Rectangle:
    def __init__(self, point_1, point_2):
        self.a = abs(point_2[0] - point_1[0])
        self.b = abs(point_2[1] - point_1[1])

    def perimeter(self):
        return round(2 * (self.a + self.b), 2)

    def area(self):
        return round(self.a * self.b, 2)
