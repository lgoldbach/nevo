import numpy as np
rand_int = np.random.randint

class Field(object):
    """Define the field on which the agents compete

    Args:
        dimensions (tuple): Dimensions of the 2D field (int).
        exp_supply (float): Expected 'food' supply. Corresponds to poisson distr.
                            lambda parameter.

    """
    def __init__(self, dimensions: tuple, exp_supply=1):
        self.field = np.zeros((dimensions[0], dimensions[1]))
        self.field = np.pad(self.field, pad_width=1, mode='constant',
                            constant_values=-1)  # add field border
        self.exp_supply = exp_supply
        self.drop_food()

    def drop_food(self):
        x, y = rand_int(1, self.field.shape[0]-1), \
               rand_int(1, self.field.shape[1]-1)

        self.field[x, y] = 1



F = Field((10,10))
f = F.field



