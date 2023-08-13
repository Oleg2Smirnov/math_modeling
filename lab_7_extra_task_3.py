import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw=2) 
xdata, ydata = [], [] 
 
ax.set_xlim(-30, 30) 
ax.set_ylim(-30, 30) 
 
def star_move(t): 
    a = np.arange(0, 18*np.pi, 0.05)
    x = 12*np.cos(a) + 8*np.cos(8*a)
    y = 12*np.sin(a) - 8*np.sin(8*a)
    xdata = x*np.cos(2*t) + y*np.sin(t)
    ydata = y*np.cos(2*t) - x*np.sin(t)
    anim_object.set_data(xdata, ydata)
    return anim_object,
 
ani = FuncAnimation(fig, 
                    star_move, 
                    frames=np.arange(0, 4*np.pi, 0.05),
                    interval=20,
                    )

ani.save('star_move.gif')
