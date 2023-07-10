import numpy as np
import lab_3_task_1 as lt1

g = lt1.earth_gravity_constant
h = 100
a = np.pi / 3
b = 30 / 180 * np.pi

v = ((g * h* (np.tan(b))**2) / (2 * (np.cos(a))**2 * (1 - np.tan(b) * np.tan(a)))) ** 0.5
print(v)


T = 200
E = 300
from lab_3_task_1 import plank_constant_2 as h2
from lab_3_task_1 import bolc_constant as k
from lab_3_task_1 import eyler_number as e
N = (2/(np.pi**0.5)) * (h2/((k*T)**3**0.5)) * (e ** (-E / (k * T))) * (E ** (T**0.5))
print(N)