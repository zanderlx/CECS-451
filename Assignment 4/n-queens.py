import sys
import random
from Board import Board

# Number of queens
n = sys.argv[1]
# Number of states
k = sys.argv[2]

states = []
for state in range(int(k)):
    random_queens = ""
    for queen in range(int(n)):
        random_queens += str(random.randint(0, int(n) - 1))
    states.append(random_queens)

for element in states:
    board = Board(int(n))
    print(element)
    board.populate(element)
    board.display()
    print("\n")
    