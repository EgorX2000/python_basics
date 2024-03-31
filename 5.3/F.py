class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if a == 0:
        if b != 0:
            return (-c / b, -c / b)
        elif c == 0:
            raise InfiniteSolutionsError
        else:
            raise NoSolutionsError
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            return (min((-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)),
                    max((-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)))
        elif d == 0:
            return (-b / (2 * a), -b / (2 * a))
        else:
            raise NoSolutionsError
