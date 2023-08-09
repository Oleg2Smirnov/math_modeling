import numpy as np
import matplotlib.pyplot as plt
import random

N = int(input('Количество ступенек: '))
def lesenka(N):
    x = np.linspace(0, N, 1000)
    y = x // 1

    plt.xlim()
    plt.ylim()
    plt.plot(x, y, label='lesenka')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('lesenka.png')

lesenka(N)
