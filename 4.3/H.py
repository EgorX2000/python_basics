def fibonacci(count):
    a = 0
    b = 1
    for _ in range(count):
        yield a
        a, b = b, a + b
