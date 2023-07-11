import numpy as np

x = int(input('Введите число строк: '))
y = int(input('Введите число столбцов: '))

a = np.zeros((x, y))

for i in range(0, x, 1):
    for j in range(0, y, 1):
        a[j, i] = input(f'Введите элемент массива {[j, i]}: ')

for j in range(0, y, 1):
    for i in range(0, x, 1):
        g = a[j, i]
        if a[j, i] > g:
            g = a[j, i]
    print(g)