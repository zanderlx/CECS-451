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

""" Fitness function getting number of non-attacking queens """
def fitness_function(board, state):
    result = 0
    col = 0

    for digit in state:
        # Last column is irrelevant
        if col is board.queens - 1: break
        
        row = int(digit) - 1
        result += check_topright(board, row, col)
        result += check_middleright(board, row, col)
        result += check_bottomright(board, row, col)
        col += 1 
    
    # Number of Non-Attacking Queens (Max Attacking Queens - Total Queens)
    return combination(board.queens) - result


def combination(queens: int):
    return math.factorial(queens) / (math.factorial(queens - 2) * math.factorial(2))


""" SELECTION """
def selection(states, fitness_probabilities):
    # Use random uniform number for probabilitiy comparison
    r = random.uniform(0, 1) 
    fitness_sum = fitness_probabilities[0]   
    for index in range(len(fitness_probabilities)):
        if r > 0 and r <= fitness_sum : return index
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


def solutionFound(states):
    # Generate new population from using genetic algorithm
    for i in range(len(states)):
        board = Board(int(n))
        board.populate(states[i])
        # Check if there is a solution in new population
        if int(fitness_function(board, states[i])) == combination(int(n)):
            print("Found Possible Solution:", states[i])
            board.display()
            return True


if __name__ == "__main__":
    # Number of queens
    n = sys.argv[1]
    # Number of states
    k = sys.argv[2]

    population = []

    print("Searching...")

    ''' --------------- INITIAL POPULATION --------------- '''

    # Generate random queen positioning
    states = set_random_queens(n, k)

    # Generate initial population
    for state in states:
        board = Board(int(n))
        board.populate(state)
        population.append(fitness_function(board, state))
    
    # Get fitness values in terms of probabilities
    fitness_probabilities = []
    [ fitness_probabilities.append(value / sum(population)) for value in population ]


    ''' --------------- GENETIC ALGORITHM --------------- '''

    numberOfCrossbreed = numberOfMutations = 0
    foundSolution = False

    # Keep searching until a solution is found
    while not foundSolution:
        # Choose random parents
        parent1 = parent2 = None

        # Check if parent1 exists
        while type(parent1) is type(None):
            parent1 = selection(states, fitness_probabilities)

        # Check if parent2 exists
        while type(parent2) is type(None):
            parent2 = selection(states, fitness_probabilities)
            # Change parent2 if it is the same as 
            # while parent2 == parent1:
            #     parent2 = selection(states, fitness_probabilities)

        # Breed selected parents
        states = crossover(states, parent1, parent2)
        numberOfCrossbreed += 1

        # Check if solution is found after breeding
        if solutionFound(states): break

        # Mutate the children
        states = mutation(states, parent1, parent2)
        numberOfMutations += 1
        
        # Check if solution is found after mutation
        if solutionFound(states): break

        generations = numberOfCrossbreed + numberOfMutations
        print("Current Generation:", generations)

    print("Total Crossbreeds:", numberOfCrossbreed)
    print("Total Mutations:", numberOfMutations)
    print("Total Generations:", generations)

    
