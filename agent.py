import numpy as np
from random import uniform as rand_unif
from random import choice
from neuralnet import NeuralNet


class Agent(object):
    def __init__(self, name: str, position: list, surround=None):
        self._position = position
        self.name = name
        self.color = [rand_unif(0, 1),
                      rand_unif(0, 1),
                      rand_unif(0, 1)]
        self.field_of_vision = surround  # sense surroundings
        self._reserves = 0
        self.nn = NeuralNet(8, 4, 2)
        self.genome = []

    def name(self):
        return self.name

    def color(self):
        return self.color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: list):
        # check if only single step is made at a time
        if sum([abs(x1-x2) for x1, x2 in zip(position, self.position)]) <= 1:
            self._position = position

    def move(self):
        ax = choice([0, 1])
        step = choice(range(-1, 2))
        if self.field_of_vision.any():
            # new_x = self.position[0] + choice(range(-1, 2))
            # new_y = self.position[1] + choice(range(-1, 2))
            new_pos = self.position.copy()
            new_pos[ax] += step
            if self.field_of_vision[new_pos[0], new_pos[1]] < 0:
                pass  # if hit wall, don't move
            else:
                # self.reserves += self.field_of_vision[new_pos[0], new_pos[1]] # eat
                self.position = new_pos


        else:
            self.position[ax] += step

    def look(self, surround):
        self.field_of_vision = surround

    @property
    def reserves(self):
        return self._reserves

    @reserves.setter
    def reserves(self, food):
        if self.reserves + food < 0:
            print(f"Reserves of {self.name}shouldn't be below 0")

        else:
            self._reserves += food



    def update_neural_net(self):
        # self.nn  = ..
        pass

    def procreate(self):
        # self.mutate() ..
        # self.genome = ..
        pass

    def mutate(self):
        # self.genome = ..
        pass

