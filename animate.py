from matplotlib import pyplot as plt
from matplotlib import animation
from simulate import simulate, make_population

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line = ax.scatter([], [])

pop = make_population(10)

# initialization function: plot the background of each frame
def init():
    line.set_offsets
    return line,

# animation function.  This is called sequentially
def animate(i):
    p = simulate(pop, 1)
    x, y, c  = [], [], []
    for cas in p:
        x.append(p[cas].position[0])
        y.append(p[cas].position[1])
        c.append(p[cas].color)

    line.set_xdata(x)
    line.set_ydata(y)

    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()