import numpy as np
import math
rand_int = np.random.randint


class Field(object):
    """Define the field on which the agents compete

    Args:
        dimensions (tuple): Dimensions of the 2D field (int).
        exp_supply (float): Expected 'food' supply. Corresponds to poisson distr.
                            lambda parameter.

    """
    def __init__(self, dimensions: tuple, exp_supply=.25):
        self.field = np.zeros((dimensions[0], dimensions[1]))
        self.field = np.pad(self.field, pad_width=1, mode='constant',
                            constant_values=-1)  # add field border
        self.exp_supply = exp_supply
        self.food = {}

    def time_step(self, population):
        for agent in population:
            c = tuple(population[agent].position)
            if self.field[c] > 0:
                self.field[c] = 0

        self.drop_food()
        for f in self.food:
            if self.food[f] == 0:  # if food is 'expired'
                self.field[f] = 0  # remove it
            else:
                self.food[f] -= 1  # decrease timer

    def drop_food(self):
        samp = math.floor(np.random.poisson(self.exp_supply))  # how much
        for i in range(samp):
            c = self.rand_coords()
            self.field[c] += 1  # where
            self.food[c] = 100  # set timer for expiration

    def remove_food(self):
        pass

    def rand_coords(self):
        x = rand_int(1, self.field.shape[0] - 1)
        y = rand_int(1, self.field.shape[1] - 1)
        return (x, y)

