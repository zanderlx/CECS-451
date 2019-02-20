import sys
import random
import math
from Board import Board

def set_random_queens(n, k):
    states = []
    for _ in range(int(k)):
        random_queens = []
        for _ in range(int(n)):
            random_queens.append((random.randint(1, int(n) - 1)))
        states.append(random_queens)
    return states


def check_topright(board, row, col):
    result = 0
    row -= 1
    col += 1
    while row >= 0 and col < board.queens:
        # print(row, col)
        if (board.spaces[row])[col] is "Q":
            result += 1
            # print("     top right", row, col)
        row -= 1
        col += 1
    return result


def check_middleright(board, row, col):
    result = 0
    for col in range(col, board.queens - 1):
        col += 1
        if (board.spaces[row])[col] is "Q":
            result += 1
            # print("     middle right", row, col)
    return result


def check_bottomright(board, row, col):
    result = 0
    for _ in zip(range(row, board.queens - 1), range(col, board.queens - 1)):
        col += 1
        row += 1
        if (board.spaces[row])[col] is "Q":
            result += 1
            # print("     bottom right", row, col)
    return result


def fitness_function(board, state):
    result = 0
    col = 0
    for digit in state:
        if col is board.queens - 1: break
        # print("Column", col)
        row = int(digit) - 1
        result += check_topright(board, row, col)
        result += check_middleright(board, row, col)
        result += check_bottomright(board, row, col)
        col += 1 
    # print("Attacking Queens:", result)
    # print("Non-Attacking Queens:", board.combination(board.queens) - result)
    
    # Number of Non-Attacking Queens (Max Attacking Queens - Total Queens)
    return combination(board.queens) - result


def combination(queens: int):
    return math.factorial(queens) / (math.factorial(queens - 2) * math.factorial(2))


# Select a random state using the fitness probabilities
# and random uniform number for comparison
def selection(states, fitness_probabilities):
    r = random.uniform(0, 1) 
    fitness_sum = fitness_probabilities[0]   
    for index in range(len(fitness_probabilities)):
        if r > 0 and r <= fitness_sum : 
            # print(states[index], r)
            return index
        fitness_sum += fitness_probabilities[index]


""" CROSSOVER """
def crossover(states, parent1, parent2):

    # print("\nBreeding")
    start = int(len(states[0]) / 2)
    end = int(len(states[0]))
    # Cross breed starting in the middle
    for position in range(start, end):
        (states[parent1])[position], (states[parent2])[position] = (states[parent2])[position], (states[parent1])[position]

    # View children after "breeding"
    # print("After:", states[parent1])
    # print("After:", states[parent2])
    # print(states)
    return states


""" MUTATION """
def mutation(states, parent1, parent2):
    # Generate mutated values
    mutated_value1 = random.randint(1, int(len(states[0])))
    mutated_value2 = random.randint(1, int(len(states[0])))

    # Generate location to apply the mutated values
    mutation_location1 = random.randint(0, int(len(states[0])) - 1)
    mutation_location2 = random.randint(0, int(len(states[0])) - 1)

    # Check if mutated value is the same value as original
    # If so, mutate again...
    if (states[parent1])[mutation_location1] == mutated_value1:
        mutated_value1 = random.randint(1, int(len(states[0])))
        (states[parent1])[mutation_location1] = mutated_value1
    (states[parent1])[mutation_location1] = mutated_value1

    # Check if mutated value is the same value as original
    # If so, mutate again...
    if (states[parent2])[mutation_location2] == mutated_value2:
        mutated_value2 = random.randint(1, int(len(states[0])))
        (states[parent2])[mutation_location2] = mutated_value2
    (states[parent2])[mutation_location2] = mutated_value2

    # print("\nMutation")
    # print("After:", states[parent1])
    # print("After:", states[parent2])

    return states


def checkBoard(states):
    for i in range(len(states)):
        board = Board(int(n))
        board.populate(states[i])
        # board.display()
        # print(states[i])
        # print("\n")
        if int(fitness_function(board, states[i])) == combination(int(n)):
            # print("\n---------------------------------------------")
            # print("Solution:", states[i])
            return True


if __name__ == "__main__":
    print("Searching...")
    # Number of queens
    n = sys.argv[1]
    # Number of states
    k = sys.argv[2]

    population = []
    fitness_values = []
    states = set_random_queens(n, k)
    # print(states)

    ''' ---------POPULATE BOARD----------------------------------------------------'''
    index = 0
    for state in states:
        board = Board(int(n))
        board.populate(state)
        # print("Board #", index, "->", state, "\n")
        # board.display()
        population.append(board)
        fitness_values.append(fitness_function(board, state))
        # print("\n")
        index += 1
    
    # Get fitness values in terms of probabilities
    fitness_probabilities = []
    for value in fitness_values: fitness_probabilities.append(value / sum(fitness_values))


    ''' --------GENETIC ALGORITHM------------------------------------------------ '''
    steps = 0
    numberOfCrossbreed = 0
    numberOfMutations = 0
    foundSolution = False
    while not foundSolution:
        # Choose random parents
        parent1 = None
        parent2 = None

        while type(parent1) is type(None):
            parent1 = selection(states, fitness_probabilities)

        while type(parent2) is type(None):
            parent2 = selection(states, fitness_probabilities)
            while parent2 == parent1:
                parent2 = selection(states, fitness_probabilities)

        


        # View parents before "breeding"
        # print("\n-------------------------------------------------")
        # print("\nOriginal")
        # # print(states)
        # print("Before:", states[parent1], parent1)
        # print("Before:", states[parent2], parent2)

        states = crossover(states, parent1, parent2)
        numberOfCrossbreed += 1
        if checkBoard(states): 
            break

        states = mutation(states, parent1, parent2)
        numberOfMutations += 1
        # print(states)
        if checkBoard(states): break


        # print(states)
    print("Total Crossbreeds:", numberOfCrossbreed)
    print("Total Mutations:", numberOfMutations)
    print("Final Total:", numberOfCrossbreed + numberOfMutations)

    # print(fitness_probabilities)
    # Get random state
    # print(selection(states, fitness_probabilities))
    
