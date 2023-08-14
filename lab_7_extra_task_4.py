import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = 10

fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw=2)
 
ax.set_xlim(-a, a)
ax.set_ylim(-a, a)
 
def square_move(alpha):
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 2, 3, 4]
    R = (2*a**2)**0.5 / 2
    for i in range(0, 4, 1):
        x[i] = R*np.cos((0.25+i/2)*np.pi + alpha)
        y[i] = R*np.sin((0.25+i/2)*np.pi + alpha)
    x[4] = R*np.cos(0.25*np.pi + alpha)
    y[4] = R*np.sin(0.25*np.pi + alpha)

    xdata = x
    ydata = y
    
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    square_move,
                    frames= np.arange(0, 2*np.pi, 0.1),
                    interval=35
                    )
 
ani.save('square_move.gif')
