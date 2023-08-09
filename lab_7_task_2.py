import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw=2) 
xdata, ydata = [0], [0] 
 
ax.set_xlim(-10*2*np.pi, 10*2*np.pi) 
ax.set_ylim(-10*2*np.pi, 10*2*np.pi) 
 
def update(frame): 
    a = np.linspace(0, 2*np.pi, 1000)
    xdata = 10 * np.cos(a) * frame  
    ydata =  10 * np.sin(a) * frame 
    anim_object.set_data(xdata, ydata)
    return anim_object,
 
ani = FuncAnimation(fig, 
                    update, 
                    frames=np.linspace(0, 2*np.pi, 1000),
                    interval=20,
                    )
 
ani.save('lab_7_task_2_circle.gif')
