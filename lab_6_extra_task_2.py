import numpy as np
import matplotlib.pyplot as plt
import random

def ellips():
    e = random.random()
    p = random.random() * 100
    a = np.linspace(0, 2*np.pi, 1000)
    r = p / (1 + e * np.cos(a))

    plt.xlim()
    plt.ylim()
    x = r * np.cos(a)
    y = r * np.sin(a)

    plt.plot(x, y, label='ellips')
    plt.legend()
    plt.title('ellips')
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('ellips.png')

ellips()
