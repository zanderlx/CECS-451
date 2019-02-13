from map import Map
import numpy as np

class Robot:
    def __init__(self):
        self.start = (0, 0)
        self.track = [self.start]

    def north_blocked(self, i):
        if i - 3 < 0: return True

    def west_blocked(self, j):
        if j - 3 < 0: return True

    def south_blocked(self, i, task):
        if i + 3 > len(task.dirty[0]) - 1: return True

    def east_blocked(self, j, task):
        if j + 3 > len(task.dirty[0]) - 1: return True

    # IMPLEMENT THIS FUNCTION
    def clean(self, task: Map):
        # FOR TESTING PURPOSES - CHECKS INITIAL DIRT AMOUNT

        total_dirty = sum(sum(task.dirty, []))
        print("Total Dirty Spots:", total_dirty, "/", total_dirty)

        # Start at (0, 0)
        row = self.start[0]
        col = self.start[0]

        # Goes through the next location after checking if
        # all sides are clean at one location. Row and col
        # get incremented by 3 to signify movement to a new
        # spot with all adjacent sides currently unobserved
        for row in range(0, len(task.dirty[0]), 3):
             # Increment movement of col by 3
            if row is not 0 or 0:
                if (row, col) is not (0, 0):
                    self.track.append((row, col))
                if (row+1, col) not in self.track:
                    self.track.append((row+1, col))
                if (row+2, col) not in self.track:
                    self.track.append((row+2, col))
                if (row+3, col) not in self.track:
                    self.track.append((row+3, col))

            for col in range(0, len(task.dirty[0]), 3):

                # If CENTER is dirty, clean CENTER
                if (task.dirty[row])[col] is 1:
                    (task.dirty[row])[col] = 0

                # Check if EAST is not blocked
                if not self.east_blocked(col, task):
                    # If EAST is dirty, clean EAST
                    if (task.dirty[row])[col+1] == 1:
                        (task.dirty[row])[col+1] = 0
                        self.track.append((row, col+1))

                # Check if SOUTH-EAST is not blocked
                if not self.east_blocked(col, task) and not self.south_blocked(row, task):
                    # If SOUTH-EAST is dirty, clean SOUTH-EAST
                    if (task.dirty[row+1])[col+1] == 1:
                        (task.dirty[row+1])[col+1] = 0
                        self.track.append((row+1, col+1))

                # Check if NORTH-EAST is not blocked
                if not self.east_blocked(col, task) and not self.north_blocked(row):
                    # If NORTH-EAST is dirty, clean NORTH-EAST
                    if (task.dirty[row-1])[col+1] == 1:
                        (task.dirty[row-1])[col+1] = 0
                        self.track.append((row-1, col+1))

                # Check if WEST is not blocked
                if not self.west_blocked(col): 
                    # If WEST is dirty, clean WEST side
                    if (task.dirty[row])[col-1] == 1:
                        (task.dirty[row])[col-1] = 0
                        self.track.append((row, col-1))

                # Check if NORTH-WEST is blocked
                if not self.north_blocked(row) and not self.west_blocked(col):
                    # If NORTH-WEST is dirty, clean NORTH-WEST 
                    if (task.dirty[row-1])[col-1] == 1:
                        (task.dirty[row-1])[col-1] = 0
                        self.track.append((row-1, col-1))
                
                # Check if SOUTH-WEST is blocked
                if not self.south_blocked(row, task) and not self.west_blocked(col):
                    # If SOUTH-WEST is dirty, clean SOUTH-WEST 
                    if (task.dirty[row+1])[col-1] == 1:
                        (task.dirty[row+1])[col-1] = 0
                        self.track.append((row+1, col-1))

                # Check if NORTH is not blocked
                if not self.north_blocked(row):
                    # If NORTH is dirty, clean NORTH 
                    if (task.dirty[row-1])[col] == 1:
                        (task.dirty[row-1])[col] = 0
                        self.track.append((row-1, col))

                # Check if SOUTH is not blocked
                if not self.south_blocked(row, task):
                    # If SOUTH is dirty, clean SOUTH 
                    if (task.dirty[row+1])[col] == 1:
                        (task.dirty[row+1])[col] = 0
                        self.track.append((row+1, col))

                if col is 0 or not 0:
                    if (row, col+1) not in self.track:
                        self.track.append((row, col+1))
                    if (row, col+2) not in self.track:
                        self.track.append((row, col+2))
                    if (row, col+3) not in self.track:
                        self.track.append((row, col+3))
        
        print(self.track)
            

        # FOR TESTING PURPOSES - CHECK FINAL DIRT AMOUNT
        print("Remaining Dirty Spots:", sum(sum(task.dirty, [])), "/", total_dirty)


    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home.show()
    agent = Robot()
    agent.clean(home)
    agent.show() # Number of steps robot took
    home.show()


# BRAINSTORMING...
# Before proceeding, check if x or y is within bounds
# ex: x >= 0 && x < len(array)  --> this applies for y as well

# Start - (list[x])[y]
# North - (list[x-1])[y]
# South - (list[x+1])[y]
# East  - (list[x])[y+1]
# West  - (list[x])[y-1]

# North-East    - (list[x-1])[y+1]
# North-West    - (list[x-1])[y-1]
# South-East    - (list[x+1])[y+1]
# South-West    - (list[x+1])[y-1]
