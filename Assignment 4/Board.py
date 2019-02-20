import math

class Board:

    def __init__(self, queens: int):
        self.queens = queens
        self.spaces = [['-' for col in range(queens)] for row in range(queens)]

    def populate(self, positions: list):
        col = 0
        for row in range(len(positions)):
            (self.spaces[int(positions[row]) - 1])[col] = "Q"
            col += 1

    def display(self):
        for element in self.spaces:
            print("[", " ".join(element), "]")

if __name__ == "__main__":
    test = "24415124"
    b = Board(len(test))
    b.populate(test)
    b.display()
    # test = '3142'
    # b.populate("24748552")
    # b.populate("32752411")
    # b.populate("24415124")
    # b.fitness("32543213")
    # b.populate("1234567891234567891")
