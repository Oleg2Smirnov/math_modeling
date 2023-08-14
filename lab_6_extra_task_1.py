import numpy as np
import matplotlib.pyplot as plt

def lissagu():
    plt.xlim()
    plt.ylim()
    t = np.linspace(0, 100, 2000)
    A, a = 1, 1
    b = 5
    B = 1.5
    d = np.pi / 2

    x = A * np.sin(a*t + d)
    y = B * np.sin(b*t)   

    plt.plot(x, y, label='lissagu')
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('lissagu.png')

lissagu()
