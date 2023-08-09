import numpy as np
import matplotlib.pyplot as plt
import random 

def cicloida():
    R = random.randint(1, 100)
    k = random.randint(50, 100)
    n = random.randint(-100, -50)
    t = np.linspace(n, k, 10000)
    plt.xlim()
    plt.ylim()

    x = R * (t - (np.sin(t)**3))
    y = R * (t - (np.cos(t)**3))

    plt.plot(x, y, label='cicloida')
    plt.legend()
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('cicloida')
    plt.savefig('cicloida.png')

def astroida():
    R = random.randint(1, 100)
    k = random.randint(50, 100)
    n = random.randint(-100, -50)
    t = np.linspace(n, k, 10000)
    plt.xlim()
    plt.ylim()

    x = R * np.cos(t)**3
    y = R * np.sin(t)**3

    plt.plot(x, y, label='astroida')
    plt.legend()
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('astroida')
    plt.savefig('astroida.png')

astroida()
