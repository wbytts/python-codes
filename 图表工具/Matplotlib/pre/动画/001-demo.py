import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_points(num):

    point_ani.set_data(x[num], y[num])
    if num%5==0:
        point_ani.set_marker("*")
        point_ani.set_markersize(12)
    else:
        point_ani.set_marker("o")
        point_ani.set_markersize(8)

    text_pt.set_position((x[num], y[num]))
    text_pt.set_text("x=%.3f, y=%.3f"%(x[num], y[num]))
    return point_ani,text_pt,


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig = plt.figure(tight_layout=True)
plt.plot(x,y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
text_pt = plt.text(4, 0.8, '', fontsize=16)

ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=100, blit=True)

# ani.save('sin_test3.gif', writer='imagemagick', fps=10)
plt.show()


