import sys
import random

# Number of queens
n = sys.argv[1]
# Number of states
k = sys.argv[2]

states = []
for state in range(int(k)):
    random_queens = ""
    for queen in range(int(n)):
        random_queens += str(random.randint(0, int(n)))
    states.append(random_queens)

print("\n".join(states))