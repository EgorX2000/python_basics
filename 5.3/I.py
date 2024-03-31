class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not all(char.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" for char in name):
        raise CyrillicError
    if not name[0].isupper() or any(char.isupper() for char in name[1:]):
        raise CapitalError

    return name


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789" for char in name):
        raise BadCharacterError
    if name[0] in "0123456789":
        raise StartsWithDigitError

    return name


def user_validation(**kwargs):
    if [arg for arg in kwargs] != ["last_name", "first_name", "username"] or len(kwargs) != 3:
        raise KeyError
    if any(not isinstance(val, str) for val in kwargs.values()):
        raise TypeError
    kwargs["last_name"] = name_validation(kwargs["last_name"])
    kwargs["first_name"] = name_validation(kwargs["first_name"])
    kwargs["username"] = username_validation(kwargs["username"])
    return kwargs
