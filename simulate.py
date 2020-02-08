from numpy.random import uniform as rand
import random
from cas import Cas

colors = ["red", "blue", "green", "yellow", "purple"]

def make_population(pop_size):
    population = {}
    for i in range(pop_size):
        name = "cas" + str(i)
        population[name] = Cas(name, [rand(-1, 1), rand(-1, 1)],
                               random.choice(colors))
    return population

def simulate(pop, steps):
    for i in range(steps):
        for cas in pop:
            pop[cas].move()
            print(cas, pop[cas].position)

    return pop

popu = make_population(2)
p = simulate(popu, 3)
for c in p:
    print(c, p[c].position)
