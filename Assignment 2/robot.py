from map import Map
import numpy as np

class Robot:
    def __init__(self):
        self.start = (0, 0)
        self.track = [self.start]

    # IMPLEMENT THIS FUNCTION
    def clean(self, task: Map):
        x = np.matrix(task)
        if (x[0])[0] is 1:
            print("Current location is dirty")
        else:
            print("Not Dirty")
         

    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home.show()
    agent = Robot()
    agent.clean(home)
    agent.show() # Number of steps robot took
    home.show()
