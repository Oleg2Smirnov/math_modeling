import numpy as np
import matplotlib.pyplot as plt 
import random

def ellips():
    a = np.linspace(0, 2*np.pi)
    e = random.random()
    p = random.randint(100, 1000)
    r = p / (1 + e * np.cos(a))
    x = r * np.cos(a)
    y = r * np.sin(a)

    plt.xlim()
    plt.ylim()
    plt.plot(x, y, label='ellips')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('ellips.png')

ellips()
