class Checkers:
    def __init__(self):
        self.desk = {
            "1": {
                "A": "W",
                "B": "X",
                "C": "W",
                "D": "X",
                "E": "W",
                "F": "X",
                "G": "W",
                "H": "X"
            },
            "2": {
                "A": "X",
                "B": "W",
                "C": "X",
                "D": "W",
                "E": "X",
                "F": "W",
                "G": "X",
                "H": "W"
            },
            "3": {
                "A": "W",
                "B": "X",
                "C": "W",
                "D": "X",
                "E": "W",
                "F": "X",
                "G": "W",
                "H": "X"
            },
            "4": {
                "A": "X",
                "B": "X",
                "C": "X",
                "D": "X",
                "E": "X",
                "F": "X",
                "G": "X",
                "H": "X"
            },
            "5": {
                "A": "X",
                "B": "X",
                "C": "X",
                "D": "X",
                "E": "X",
                "F": "X",
                "G": "X",
                "H": "X"
            },
            "6": {
                "A": "X",
                "B": "B",
                "C": "X",
                "D": "B",
                "E": "X",
                "F": "B",
                "G": "X",
                "H": "B"
            },
            "7": {
                "A": "B",
                "B": "X",
                "C": "B",
                "D": "X",
                "E": "B",
                "F": "X",
                "G": "B",
                "H": "X"
            },
            "8": {
                "A": "X",
                "B": "B",
                "C": "X",
                "D": "B",
                "E": "X",
                "F": "B",
                "G": "X",
                "H": "B"
            }
        }

    def move(self, f, t):
        color = self.desk[f[1]][f[0]]
        self.desk[f[1]][f[0]] = "X"
        self.desk[t[1]][t[0]] = color

    def get_cell(self, p):
        return Cell(self.desk[p[1]][p[0]])


class Cell:
    def __init__(self, coords):
        self.coords = coords

    def status(self):
        return self.coords
