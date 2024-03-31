class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789" for char in name):
        raise BadCharacterError
    if name[0] in "0123456789":
        raise StartsWithDigitError

    return name
