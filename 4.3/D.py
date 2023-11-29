def answer(func):
    def wrapper(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"

    return wrapper
