import numpy as np
from random import uniform as rand_unif


class Agent:
    def __init__(self, name, p):
        self.position = p
        self.name = name
        self.color = [rand_unif(0, 1),
                      rand_unif(0, 1),
                      rand_unif(0, 1)]

    def name(self):
        return self.name

    def position(self):
        return self.position

    def color(self):
        return self.color

    def move(self):
        x_add, y_add = np.random.normal(0, .05), np.random.normal(0, .05)
        p = self.position
        p[0] += x_add
        p[1] += y_add

        self.position = p
