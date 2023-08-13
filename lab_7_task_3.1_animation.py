import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw=2)
 
xdata, ydata = [], []
 
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
 
def update(t):
    xdata.append(np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12))**5))
    ydata.append(np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12))**5))
    anim_object.set_data(xdata, ydata)
    return anim_object,
 
ani = FuncAnimation(fig,
                    update,
                    frames=np.linspace(0, 12*np.pi, 800),
                    interval=75
                    )
 
ani.save('butterfly.gif')
