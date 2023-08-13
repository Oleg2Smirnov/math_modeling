import numpy as np
import matplotlib.pyplot as plt 

def rose_spiral():
    b = 2
    a = np.linspace(0, 8*np.pi, 10000)
    r = np.sin(a*b)
    x = r * np.cos(a)
    y = r * np.sin(a)

    plt.xlim()
    plt.ylim()
    plt.plot(x, y, label='rose_spiral')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('rose_spiral.png')

rose_spiral()
