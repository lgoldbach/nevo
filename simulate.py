from numpy import random as rand
import random
from agent import Agent
from field import Field


def make_population(pop_size, borders: tuple):
    population = {}
    for i in range(pop_size):
        name = "agent" + str(i)
        population[name] = Agent(name, [random.choice(range(1, borders[0])),
                                        random.choice(range(1, borders[1]))],)
    return population

def simulate(pop, field, steps):
    for i in range(steps):
        for agent in pop:
            pop[agent].look(field.field)  # observe field
            pop[agent].move()  # make move
        field.time_step(pop)  # update field
    return pop

