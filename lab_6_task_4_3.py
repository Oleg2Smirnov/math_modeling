import numpy as np
import matplotlib.pyplot as plt 

def gezl_spiral():
    b = 0.1
    a = np.linspace(0.05, 8*np.pi, 10000)
    r = b / (a ** 0.5)
    x = r * np.cos(a)
    y = r * np.sin(a)

    plt.xlim()
    plt.ylim()
    plt.plot(x, y, label='gezl_spiral')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('gezl_spiral.png')

gezl_spiral()
