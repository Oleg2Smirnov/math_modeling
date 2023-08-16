import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object2, = plt.plot([], [], '-', lw=2, color='lime', label='cicloida')
anim_object1, = plt.plot([], [], '-', lw=2, color='b', label='road')
anim_object3, = plt.plot([], [], '-', lw=2, color='dodgerblue', label='circle')
anim_object4, = plt.plot([], [], '-', lw=2, color='k', label='line')
anim_object5, = plt.plot([], [], '-', lw=2, color='k', label='dot')

plt.axis('equal')
plt.xlim(-10, 4*np.pi*10+10)
plt.ylim(-10, 31.59155*np.pi)

x1, y1 = [0, 125.664], [0, 0]
x2, y2 = [], []
y3, x31 = [], []
alpha = np.linspace(0, 2*np.pi, 500)
x31.append(10*(1+np.cos(alpha))-10)
y3.append(10*(1+np.sin(alpha)))
a = [0]
x4 = [0, 0]
y4 = [10, 0]
x51, y51 = [], []
x51.append(0.5*(1+np.cos(alpha))-0.5)
y51.append(0.5*(1+np.sin(alpha))-0.5)

def func(t):
    R = 10
    T = np.linspace(0, 4*np.pi, 1000)
    x2.append(R * (T - np.sin(T)))
    y2.append(R * (1 - np.cos(T)))
    x3 = x31 + t
    x4[0] = t
    x4[1] = R * (t/10 - np.sin(t/10))
    y4[1] = R * (1 - np.cos(t/10))
    x5 = x51 + R * (t/10 - np.sin(t/10))
    y5 = y51 + R * (1 - np.cos(t/10))

    anim_object2.set_data(x2, y2)
    anim_object1.set_data(x1, y1)
    anim_object3.set_data(x3, y3)
    anim_object4.set_data(x4, y4)
    anim_object5.set_data(x5, y5)
    return anim_object2, anim_object1, anim_object3,anim_object4, anim_object5,

ani = FuncAnimation(fig,
                    func,
                    frames=np.arange(0, 125.664, 1),
                    interval=35,
                    )

ani.save('cicloida.gif')
