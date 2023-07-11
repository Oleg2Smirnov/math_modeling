import numpy as np

n = int(input('Введите количество строк: '))
N = float(input('N = '))
M = float(input('M = '))
a = np.zeros((n, 2))

for j in range(0, n, 1):
    for i in range(0, 2, 1):
        a[j, i] = np.sin(N * (i+1) + M * (j+1))
        if a[j, i] < 0:
            a[j, i] = 0
print(a)