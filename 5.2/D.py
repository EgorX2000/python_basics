import math


class Fraction():
    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.den = map(int, args[0].split(sep="/"))
        elif len(args) == 2:
            self.num, self.den = args

    def __simplify(self):
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    def numerator(self, number=0):
        if number:
            self.num = number

        self.__simplify()
        return self.num

    def denominator(self, number=0):
        if number:
            self.den = number

        self.__simplify()
        return self.den

    def __str__(self):
        self.__simplify()
        return f"{self.num}/{self.den}"

    def __repr__(self):
        self.__simplify()
        return f"Fraction({self.num}, {self.den})"
