class Broken:
    def __repr__(self):
        raise Exception


def func():
    pass


func(Broken())
