from matplotlib import pyplot as plt
from matplotlib import animation
from simulate import simulate, make_population
from field import Field
import numpy as np


# Set field and generate population
f = Field((14, 10))
pop = make_population(1, np.subtract(f.field.shape, (2,2)))
colors = [pop[agent].color for agent in pop]  # get agent colors

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()

# Aesthetics
# Set 10x10 grid without axes labels and ticks
ax = plt.axes(xlim=(0, f.field.shape[1]-0.5), ylim=(0, f.field.shape[0]-0.5))
ax.set_aspect('equal')  # make sure it is square
ax.set_yticks(np.arange(0, f.field.shape[0])-0.5, minor=True)
ax.set_xticks(np.arange(0, f.field.shape[1])-0.5, minor=True)
ax.tick_params(axis=u'both', which=u'both', length=0)
ax.grid(True, which="minor", color='black')

plt.xticks([], [])
plt.yticks([], [])
plt.gca().invert_yaxis() # to match numpy array

## color borders
plt.fill_between(np.arange(-0.5, f.field.shape[1]+.5, 1),
                 .5,
                 [-.5]*(f.field.shape[1]+1),
                 color='black')
plt.fill_between(np.arange(-0.5, f.field.shape[1]+.5, 1),
                 f.field.shape[0]-1.5,
                 [f.field.shape[0]-.5]*(f.field.shape[1]+1),
                 color='black')
plt.fill_betweenx(np.arange(-0.5, f.field.shape[0]+.5, 1),
                 f.field.shape[1]-1.5,
                 [f.field.shape[1]-.5]*(f.field.shape[0]+1),
                 color='black')
plt.fill_betweenx(np.arange(-0.5, f.field.shape[0]+.5, 1),
                 .5,
                 [-.5]*(f.field.shape[0]+1),
                 color='black', edgecolor='black')

# Scatter plot for agents
line = ax.scatter([], [], c=colors, edgecolor='black', s=150, linewidth=1)


# initialization function: plot the background of each frame
def init():
    line.set_offsets(np.c_[[], []])
    return line,


def animate(i):
    p = simulate(pop, f, 1)
    x, y, c = [], [], []   # clear lists.
    for agent in p:
        x.append(p[agent].position[1])  # x and y flipped to match numpy array
        y.append(p[agent].position[0])

    line.set_offsets(np.c_[x, y])

    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=10,
                               interval=1000, blit=True)

anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()