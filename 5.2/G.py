class Fraction:

    def __simplify(self, coords):
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.num, self.den = self.__simplify(
                tuple(map(int, args[0].split('/'))))
        else:
            self.num, self.den = self.__simplify(args)

    def numerator(self, number=0):
        if number:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(number), self.den))
                self.num = -self.num if number < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(number), self.den))
                self.num = -self.num if number > 0 else self.num
        return abs(self.num)

    def denominator(self, number=0):
        if number:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(number)))
                self.num = -self.num if number < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify(
                    (abs(self.num), abs(number)))
                self.num = -self.num if number > 0 else self.num
        return self.den

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __iadd__(self, other):
        self.num, self.den = self.__simplify(
            (self.num * other.den + other.num * self.den, self.den * other.den))
        return self

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __isub__(self, other):
        self.num, self.den = self.__simplify(
            (self.num * other.den - other.num * self.den, self.den * other.den))
        return self

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __imul__(self, other):
        self.num, self.den = self.__simplify(
            (self.num * other.num, self.den * other.den))
        return self

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other):
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num))
        return self

    def reverse(self):
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.den}')"
