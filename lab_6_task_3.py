import numpy as np
import random
import matplotlib.pyplot as plt

xfirst = float(input('Минимальное значение x: '))
xlast = float(input('Максимальное значение x: '))
N = int(input('Количество точек: '))

a = random.randint(1, xlast)
b = random.randint(1, a)
 
def ellips_plotter(a=1, b=1, title = 'ellips_plotter'):
    
    x = np.linspace(xfirst, xlast, N)
    y = np.linspace(-2*b, 2*b, N)

    X, Y = np.meshgrid(x, y)
  
    fxy = X**2 / a**2 + Y**2 / b**2

    plt.plot(x, y, label='my ellips')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.contour(X, Y, fxy, levels=[1])
    plt.savefig('lab_6_task_3.png')

ellips_plotter(a, b)
