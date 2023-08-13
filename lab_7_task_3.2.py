import numpy as np
import matplotlib.pyplot as plt 

def heart():
    t = np.linspace(0, 2*np.pi, 10000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.plot(x, y, label='heart')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('heart.png')

heart()
