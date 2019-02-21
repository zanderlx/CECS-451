
class Board:

    """ Initialize board """
    def __init__(self, queens: int):
        self.queens = queens
        self.spaces = [[u"\u2022" for col in range(queens)] for row in range(queens)]

    """ Populate board using list """
    def populate(self, positions: list):
        col = 0
        for row in range(len(positions)):
            (self.spaces[int(positions[row]) - 1])[col] = "Q"
            col += 1

    """ Display the board instance """
    def display(self):
        for element in self.spaces:
            print("[", " ".join(element), "]")

if __name__ == "__main__":
    test = "24415124"
    b = Board(len(test))
    b.populate(test)
    b.display()
