def result_accumulator(func):
    result = list()

    def wrapper(*args, method="accumulate"):
        if method == "accumulate":
            result.append(func(*args))
        elif method == "drop":
            ans = result + [func(*args)]
            result.clear()
            return ans
    return wrapper
