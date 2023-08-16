import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object1, = plt.plot([], [], '-', lw=2, color='b', label='circle')
anim_object2, = plt.plot([], [], '-', lw=2, color='lime', label='astroida')
anim_object3, = plt.plot([], [], '-', lw=2, color='magenta', label='small_circle')
anim_object4, = plt.plot([], [], '-', lw=2, color='k', label='line')
anim_object5, = plt.plot([], [], '-', lw=2, color='k', label='dot')

plt.axis('equal')
plt.xlim(-20, 20)
plt.ylim(-15, 15)

def astroida(t):
    R = 10
    n = np.linspace(0, 2*np.pi, 300)
    x1 = R * np.cos(n)
    y1 = R * np.sin(n)
    x2 = R * np.cos(n)**3
    y2 = R * np.sin(n)**3
    x31 = 2.5 * np.cos(n)
    y31 = 2.5 * np.sin(n)
    x3 = x31 + 7.5*np.cos(t)
    y3 = y31 + 7.5*np.sin(t)
    x4 = [0, 0]
    y4 = [0, 0]
    x4[0] = 7.5 * np.cos(t)
    y4[0] = 7.5 * np.sin(t)
    x4[1] = 7.5*np.cos(t) + 2.5*np.cos(-t*3) 
    y4[1] = 7.5*np.sin(t) + 2.5*np.sin(-t*3) 
    x51 = 0.2*np.cos(n)
    y51 = 0.2*np.sin(n)
    x5 = 7.5*np.cos(t) + 2.5*np.cos(-t*3) + x51
    y5 = 7.5*np.sin(t) + 2.5*np.sin(-t*3) + y51

    anim_object1.set_data(x1, y1)
    anim_object2.set_data(x2, y2)
    anim_object3.set_data(x3, y3)
    anim_object4.set_data(x4, y4)
    anim_object5.set_data(x5, y5)
    return anim_object1, anim_object2, anim_object3, anim_object4, anim_object5,

ani = FuncAnimation(fig,
                    astroida,
                    frames=np.linspace(0, 2*np.pi, 300),
                    interval=35,
                    )

ani.save('astroida.gif')
