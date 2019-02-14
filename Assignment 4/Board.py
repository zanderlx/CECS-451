class Board:
    def __init__(self, queens: int):
        self.spaces = [["-" for i in range(queens)] for k in range(queens)]

    def populate(self, positions: str):
        i = 0
        for n in range(len(positions)):
            (self.spaces[int(positions[n])])[i] = "Q"
            i += 1

    def display(self):
        for l in self.spaces:
            print(l)


if __name__ == "__main__":
    b = Board(8)
    b.populate("21432101")
    b.display()
