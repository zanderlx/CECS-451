
class Board:

    def __init__(self, queens: int):
        self.spaces = [["-" for col in range(queens)] for row in range(queens)]


    def populate(self, positions: str):
        col = 0
        for row in range(len(positions)):
            (self.spaces[int(positions[row]) - 1])[col] = "Q"
            col += 1


    def display(self):
        for element in self.spaces:
            print(element)


    def check_topright(self, row, col):
        result = 0
        for _ in zip(range(row, -1, -1), range(col, 7, 1)):
            col += 1
            row -= 1
            if (self.spaces[row])[col] is "Q":
                result += 1
                # print("     top right", row, col)
        return result


    def check_middleright(self, row, col):
        result = 0
        
        for col in range(col, 7):
            col += 1
            if (self.spaces[row])[col] is "Q":
                result += 1
                # print("     middle right", row, col)
        return result


    def check_bottomright(self, row, col):
        result = 0
        for _ in zip(range(row, 7), range(col, 7)):
            col += 1
            row += 1
            if (self.spaces[row])[col] is "Q":
                result += 1
                # print("     bottom right", row, col)
        return result
        

    def fitness(self, state):
        result = 0
        col = 0
        for digit in state:
            if col is 7: break
            # print("Column", col)
            row = int(digit) - 1
            result += self.check_topright(row, col)
            result += self.check_middleright(row, col)
            result += self.check_bottomright(row, col)
            col += 1 
        # print("Attacking Queens:", result)
        print("Non-Attacking Queens:", 28 - result)

if __name__ == "__main__":
    b = Board(8)
    
    # b.populate("24748552")
    # b.populate("32752411")
    # b.populate("24415124")
    b.populate("32543213")
    b.display()
    b.fitness("32543213")
    # b.populate("01234567890123456780123456789012345678")
