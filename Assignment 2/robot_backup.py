from map import Map
import numpy as np

class Robot:
    def __init__(self):
        self.start = (0, 0)
        self.track = [self.start]

    # IMPLEMENT THIS FUNCTION
    def clean(self, task: Map):
        total_dirty = sum(sum(task.dirty, []))
        print("Total Dirty Spots:", total_dirty, "/", total_dirty)
        for i in range(len(task.dirty)):
            for j in range(len(task.dirty[0])):
        # i = self.start[0]
        # j = self.start[0]
                if (task.dirty[i])[j] is 1:
                    (task.dirty[i])[j] = 0
                if (i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(task.dirty) and j + 1 < len(task.dirty[0])):
                    # NORTH
                    if (task.dirty[i-1])[j] is 1:
                        i -= 1
                        (task.dirty[i])[j] = 0
                    # NORTH EAST
                    elif (task.dirty[i-1])[j-1] is 1:
                        i -= 1
                        j -= 1
                        (task.dirty[i])[j] = 0
                    # EAST
                    elif (task.dirty[i])[j+1] is 1:
                        j += 1
                        (task.dirty[i])[j] = 0
                    # SOUTH EAST
                    elif (task.dirty[i+1])[j-1] is 1:
                        i += 1
                        j -= 1
                        (task.dirty[i])[j] = 0
                    # SOUTH
                    elif (task.dirty[i+1])[j] is 1:
                        i += 1
                        (task.dirty[i])[j] = 0
                    # SOUTH WEST
                    elif (task.dirty[i+1])[j+1] is 1:
                        i += 1
                        j += 1
                        (task.dirty[i])[j] = 0
                    # WEST
                    elif (task.dirty[i])[j-1] is 1:
                        j -= 1
                        (task.dirty[i])[j] = 0
                    # NORTH WEST
                    elif (task.dirty[i-1])[j+1] is 1:
                        i -= 1
                        j += 1
                        (task.dirty[i])[j] = 0
                    else:
                        print((i, j), "Zeros around me")
        


                        

                    self.track.append((i, j))
        print(self.track)

        print("Remaining Dirty Spots:", sum(sum(task.dirty, [])), "/", total_dirty)
        # print(self.track)

    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home.show()
    agent = Robot()
    agent.clean(home)
    agent.show() # Number of steps robot took
    home.show()

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

# [[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 1 0 0 0 1 0 1 1 1 1 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 1 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0]
#  [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]]
