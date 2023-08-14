import numpy as np
import matplotlib.pyplot as plt
import random

a = random.randint(-100, 0)
b = random.randint(0, 100)

def func(c, d):
    x = []
    y = []
    for t1 in range(-200, c, 1):
        x.append(t1)
        y.append(c**2)
    for t2 in range(c, d+1, 1):
        x.append(t2)
        y.append(t2**2)
    for t3 in range(d, 200, 1):
        x.append(t3)
        y.append(d**2)

    plt.plot(x, y, label='function')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('lab_6_task_3.png')

func(a, b)
