import sys
import random
import math
import time
from Board import Board

""" Generate random queen positons """
def set_random_queens(n, k):
    states = []
    for _ in range(int(k)):
        random_queens = []
        for _ in range(int(n)):
            random_queens.append((random.randint(1, int(n) - 1)))
        states.append(random_queens)
    return states

""" Check every space to the the top-right of current queen """
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

""" Check every space to the the middle-right of current queen """
def check_middleright(board, row, col):
    result = 0
    for col in range(col, board.queens - 1):
        col += 1
        if (board.spaces[row])[col] is "Q":
            result += 1
            # print("     middle right", row, col)
    return result

""" Check every space to the the bottom-right of current queen """
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
def fitness_function(board, state, max_attacking_queens):
    result = col =0

    for digit in state:
        # Last column is irrelevant
        if col is board.queens - 1: break
        
        row = int(digit) - 1
        # Check attacking queens in top-right
        result += check_topright(board, row, col)
        # Check attacking queens in middle-right
        result += check_middleright(board, row, col)
        # Check attacking queens in bottom-right
        result += check_bottomright(board, row, col)
        col += 1 
    
    # Number of Non-Attacking Queens (Max Attacking Queens - Total Queens)
    return max_attacking_queens - result

""" Combination formula """
def combination(queens: int):
    return math.factorial(queens) / (math.factorial(queens - 2) * math.factorial(2))


""" SELECTION """
def selection(states, fitness_probabilities):
    # Use random uniform number for probabilitiy comparison
    r = random.uniform(0, 1) 
    fitness_sum = fitness_probabilities[0]   
    for index in range(len(fitness_probabilities)):
        # If random uniform number is within range return the value
        if r > 0 and r <= fitness_sum : return index
        fitness_sum += fitness_probabilities[index]


""" CROSSOVER """
def crossover(states, parent1, parent2):
    # print("\nBreeding")

    # Start in the middle of a state
    start = int(len(states[0]) / 2)
    # End till length of a state
    end = int(len(states[0]))

    # Cross breed starting in the middle
    for position in range(start, end):
        (states[parent1])[position], (states[parent2])[position] = (states[parent2])[position], (states[parent1])[position]

    # View children after "breeding"
    # print("After:", states[parent1])
    # print("After:", states[parent2])

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

""" Check if solution has been found in current generation """
def solutionFound(states, generation, max_attacking_queens):
    # Generate new population from using genetic algorithm
    for i in range(len(states)):
        board = Board(int(n))
        board.populate(states[i])
        # Check if there is a solution in new population
        if int(fitness_function(board, states[i], max_attacking_queens)) == combination(int(n)):
            # print("Current Generation:", generation)
            print("\nFound Possible Solution:", states[i])
            board.display()
            return True

""" --------------- START PROGRAM --------------- """

if __name__ == "__main__":
    # Number of queens
    n = sys.argv[1]
    # Number of states
    k = sys.argv[2]

    # Max number of attacking queens for given n (calculated once)
    max_attacking_queens = combination(int(n))

    # Board number is too small to accomodate queens
    if int(n) < 4:
        print("No possible solutions for", n, "queens in a", n, "x", n, "board!")
        sys.exit()

    # Initial population
    population = []

    ''' --------------- INITIAL POPULATION --------------- '''

    # Generate random queen positioning
    states = set_random_queens(n, k)

    # Generate initial population
    for state in states:
        board = Board(int(n))
        board.populate(state)
        population.append(fitness_function(board, state, max_attacking_queens))
    
    # Get fitness values in terms of probabilities
    fitness_probabilities = []
    [ fitness_probabilities.append(value / sum(population)) for value in population ]


    ''' --------------- GENETIC ALGORITHM --------------- '''

    numberOfCrossbreed = numberOfMutations = generation = 0
    foundSolution = False
    # Choose random parents
    parent1 = parent2 = None

    # Keep searching until a solution is found
    while not foundSolution:

        # Console logging (NOTE: Remove to see output instantly)
        print("Searching Generation:", generation + 1, end="\r")
        # Remove this to see output instantly
        time.sleep(0.001) # Delays output bu 0.1 seconds


        """ SELECTION """
        # Check if parent1 does not exist
        while type(parent1) is type(None):
            # Find another parent2
            parent1 = selection(states, fitness_probabilities)

        # Check if parent2 does not exist
        while type(parent2) is type(None):
            # Find another parent2
            parent2 = selection(states, fitness_probabilities)

        """ CROSSOVER / BREEDING """
        states = crossover(states, parent1, parent2)
        numberOfCrossbreed += 1

        # Generation does not include mutation because it is part of
        # the same generation
        generation = numberOfCrossbreed

        # Check if solution is found after breeding
        if solutionFound(states, generation, max_attacking_queens): break

        """ MUTATION """
        states = mutation(states, parent1, parent2)
        numberOfMutations += 1

        # Check if solution is found after mutation
        if solutionFound(states, generation, max_attacking_queens): break   



    """ --------------- SOLUTION --------------- """
    print("\nTotal Crossbreeds:", numberOfCrossbreed)
    
    """ 
        NOTE: If mutations is less than the number of crossbreeds
        then the solution was found before mutation 
    """
    print("Total Mutations:", numberOfMutations)

    print("Total Generations:", generation)

    
