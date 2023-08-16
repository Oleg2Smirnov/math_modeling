import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2, color='b', label='square')

plt.axis('equal')
plt.xlim(-10, 10)
plt.ylim(-10, 10)

def square(t):
    a = np.pi
    x = [5*np.cos(t), 5*np.cos(t+0.5*a), 5*np.cos(t+a), 5*np.cos(t+1.5*a), 5*np.cos(t)]
    y = [5*np.sin(t), 5*np.sin(t+0.5*a), 5*np.sin(t+a), 5*np.sin(t+1.5*a), 5*np.sin(t)]

    anim_object.set_data(x, y)
    return anim_object,

ani = FuncAnimation(fig,
                    square,
                    frames=np.arange(0, 2*np.pi, 0.05),
                    interval=20)

ani.save('square.gif')
