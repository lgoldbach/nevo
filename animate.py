from matplotlib import pyplot as plt
from matplotlib import animation
from simulate import simulate, make_population
from field import Field
import numpy as np


# Set field and generate population
f = Field((100, 140))
pop = make_population(5, np.subtract(f.field.shape, (2,2)))
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
agents = ax.scatter([], [], c=colors, edgecolor='black', s=150, linewidth=1)
food = ax.scatter([], [], c='black', marker='x')

# initialization function: plot the background of each frame
def init():
    agents.set_offsets(np.c_[[], []])
    food.set_offsets(np.c_[[], []])
    return agents, food,


def animate(i):
    # advance simulation by one step
    p = simulate(pop, f, 1)

    # update agent coordinates
    a_x, a_y, c = [], [], []   # clear lists.
    for agent in p:
        a_x.append(p[agent].position[1])  # x and y flipped to match numpy arr.
        a_y.append(p[agent].position[0])
    agents.set_offsets(np.c_[a_x, a_y])  # np.c_ is  zip for arrays (I think)

    # update food coordinates
    f_y, f_x = np.where(f.field > 0)  # x and y flipped to match numpy array
    food.set_offsets(np.c_[f_x, f_y])

    return agents, food,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=300,
                               interval=5000, blit=True)

anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
print('Finished animation')

plt.show()
