def func():
    x = int('Hello, world!')


try:
    func()
    print("No Exceptions")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")
