import numpy as np


class Cas:
    def __init__(self, name, p, c):
        self.position = p
        self.color = c
        self.name = name

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
