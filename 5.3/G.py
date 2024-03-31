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
