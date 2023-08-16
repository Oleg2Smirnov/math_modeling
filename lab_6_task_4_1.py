import numpy as np
import matplotlib.pyplot as plt 

def spiral():
    b = 0.1
    a = np.linspace(0, 8*np.pi, 10000)
    r = np.exp(b*a)
    x = r * np.cos(a)
    y = r * np.sin(a)

    plt.xlim()
    plt.ylim()
    plt.plot(x, y, label='spiral')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('spiral.png')

spiral()
