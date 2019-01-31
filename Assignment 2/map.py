import random
import numpy as np


class Map:
    def __init__(self, width, height):
        self.dirty = [[random.randint(0, 1) for i in range(height)] for j in range(width)]

    def show(self):
        print(np.matrix(self.dirty))

    def is_dirty(self):
        if sum(sum(self.dirty, [])) > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Map(19, 19)
    test.show()
    print(test.is_dirty())

