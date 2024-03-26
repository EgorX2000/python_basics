class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, point):
        return round((abs(self.x - point.x) ** 2 + abs(self.y - point.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if len(args) == 0:
            x = y = 0
        elif len(args) == 1:
            x, y = args[0]
        elif len(args) == 2:
            x, y = args

        Point.__init__(self, x, y)

    def __str__(self):
        return f"{(self.x, self.y)}"

    def __repr__(self):
        return f"PatchedPoint{(self.x, self.y)}"

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self
