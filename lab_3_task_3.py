import numpy as np

from lab_3_task_1 import earth_gravity_constant as g
x0 = float(input('Начальная координата x: '))
y0 = float(input('Начальная координата y: '))
vox = float(input('Скорость тела по оси x: '))
voy = float(input('Скорость тела по оси y: '))
n = int(input('Количество точек времени: '))
a = np.ones((n, 3))
b = 0
for t in np.linspace(0, 5, n+1):
    a[b, 0] = t
    x = x0 + vox * t
    a[b, 1] = x
    y = y0 + voy * t - g * t ** 2 / 2
    a[b, 2] = y
    b += 1
print(a)
