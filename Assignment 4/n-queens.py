import sys
import random
from Board import Board

def set_random_queens(n, k):
    states = []
    for _ in range(int(k)):
        random_queens = ""
        for _ in range(int(n)):
            random_queens += str(random.randint(1, int(n) - 1))
        states.append(random_queens)
    return states

if __name__ == "__main__":
    # Number of queens
    n = sys.argv[1]
    # Number of states
    k = sys.argv[2]

    fitness_values = []
    for state in set_random_queens(n, k):
        board = Board(int(n))
        board.populate(state)
        board.display()
        board.fitness(state)
        print("\n")
        
