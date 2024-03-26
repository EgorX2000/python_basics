class Fraction:

    def __simplify(self, coords):
        if len(coords) == 1:
            coords += (1,)
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
                self.num, self.den = self.__simplify(
                    (abs(number), self.den))
                self.num = -self.num if number < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify(
                    (abs(number), self.den))
                self.num = -self.num if number > 0 else self.num
        return abs(self.num)

    def denominator(self, number=0):
        if number:
            if self.num > 0:
                self.num, self.den = self.__simplify(
                    (self.num, abs(number)))
                self.num = -self.num if number < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify(
                    (abs(self.num), abs(number)))
                self.num = -self.num if number > 0 else self.num
        return self.den

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        temp = self.__simplify((num, den))
        return Fraction(temp[0], temp[1])

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        temp = self.__simplify((num, den))
        self.num = temp[0]
        self.den = temp[1]
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = other.num * self.den + self.num * other.den
        den = self.den * other.den
        temp = self.__simplify((num, den))
        return Fraction(temp[0], temp[1])

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        temp = self.__simplify((num, den))
        return Fraction(temp[0], temp[1])

    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        temp = self.__simplify((num, den))
        self.num = temp[0]
        self.den = temp[1]
        return self

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = other.num * self.den - self.num * other.den
        den = self.den * other.den
        temp = self.__simplify((num, den))
        return Fraction(temp[0], temp[1])

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.num
        den = self.den * other.den
        temp = self.__simplify((num, den))
        return Fraction(temp[0], temp[1])

    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.num
        den = self.den * other.den
        temp = self.__simplify((num, den))
        self.num = temp[0]
        self.den = temp[1]
        return self

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.num
        den = self.den * other.den
        temp = self.__simplify((num, den))
        return Fraction(temp[0], temp[1])

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num))
        return self

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(other.num * self.den, other.den * self.num)

    def reverse(self):
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den >= other.num * self.den

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den <= other.num * self.den

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den != other.num * self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.den}')"
