def same_type(func):
    def wrapper(*args):
        tp = type(args[0])
        for arg in args:
            if type(arg) is not tp:
                print("Обнаружены различные типы данных")
                return "Fail"
        return func(*args)
    return wrapper
