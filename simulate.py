from numpy.random import uniform as rand
from agent import Agent


def make_population(pop_size):
    population = {}
    for i in range(pop_size):
        name = "agent" + str(i)
        population[name] = Agent(name, [rand(-1, 1), rand(-1, 1)],)
    return population

def simulate(pop, steps):
    for i in range(steps):
        for Agent in pop:
            pop[Agent].move()

    return pop

popu = make_population(2)
p = simulate(popu, 3)

