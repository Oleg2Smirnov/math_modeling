import numpy as np
import random 
import matplotlib.pyplot as plt

xfirst = float(input('Минимальное значение x: '))
xlast = float(input('Максимальное значение x: '))
N = int(input('Количество точек: '))
a = random.randint(-100, 100)

def hyperbola_plotter(a=1, title='Hyperbola_plotter'):
    x = np.linspace(xfirst, xlast, N)
    y = a/x
 
    plt.plot(x, y, label='my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig('lab_6_task_2.png')
	
hyperbola_plotter(a)
