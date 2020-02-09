from numpy.random import uniform as rand
from cas import Cas


def make_population(pop_size):
    population = {}
    for i in range(pop_size):
        name = "cas" + str(i)
        population[name] = Cas(name, [rand(-1, 1), rand(-1, 1)],)
    return population

def simulate(pop, steps):
    for i in range(steps):
        for cas in pop:
            pop[cas].move()

    return pop

popu = make_population(2)
p = simulate(popu, 3)

