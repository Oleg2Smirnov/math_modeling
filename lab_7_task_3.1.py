import numpy as np
import matplotlib.pyplot as plt 

def butterfly():
    t = np.linspace(0, 12*np.pi, 10000)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12))**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12))**5)

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.plot(x, y, label='butterfly')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('butterfly.png')

butterfly()
