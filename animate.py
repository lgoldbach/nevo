from matplotlib import pyplot as plt
from matplotlib import animation
from simulate import simulate, make_population
import numpy as np


pop = make_population(10)

colors = [pop[cas].color for cas in pop]

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line = ax.scatter([], [], c=colors, edgecolor='black', linewidth=1)


# initialization function: plot the background of each frame
def init():
    line.set_offsets(np.c_[[], []])
    return line,


def animate(i):
    p = simulate(pop, 1)
    x, y, c = [], [], []   # clear lists.
    for cas in p:
        x.append(p[cas].position[0])
        y.append(p[cas].position[1])

    line.set_offsets(np.c_[x, y])

    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()