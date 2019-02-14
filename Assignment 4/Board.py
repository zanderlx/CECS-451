class Board:
    def __init__(self, queens: int):
        self.spaces = [["-" for i in range(queens)] for k in range(queens)]

    def populate(self, positions: list):
        i = 0
        for n in positions:
            (self.spaces[n])[i] = "Q"
            i += 1

    def display(self):
        for l in self.spaces:
            print(l)


if __name__ == "__main__":
    b = Board(8)
    b.populate([2, 1, 4, 3, 2, 1, 0, 2])
    b.display()
