import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw=2) 
 
def update(R): 
    a = np.linspace(0, 2*np.pi, 100)
    xdata = np.cos(a) * R  
    ydata = np.sin(a) * R 
    anim_object.set_data(xdata, ydata)

plt.axis('equal')
ax.set_xlim(-100, 100) 
ax.set_ylim(-100, 100) 

ani = FuncAnimation(fig, 
                    update, 
                    frames=150,
                    interval=20,
                    )
 
ani.save('lab_7_task_2_circle.gif')
