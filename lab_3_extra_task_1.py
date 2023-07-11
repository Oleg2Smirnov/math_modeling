import numpy as np

x = int(input('Введите число строк: '))
y = int(input('Введите число столбцов: '))

a = np.zeros((x, y))
b = np.zeros((x, y))
c = np.zeros((x, y))

for i in range(0, x, 1):
    for j in range(0, y, 1):
        a[j, i] = input(f'Введите элемент массива a{[j, i]}: ')

for i in range(0, x, 1):
    for j in range(0, y, 1):
        b[j, i] = input(f'Введите элемент массива b{[j, i]}: ')

for i in range(0, x, 1):
    for j in range(0, y, 1):
        if a[j, i] > b[j, i]:
            c[j, i] = a[j, i]
        else:
            c[j, i] = b[j, i]