import numpy as np

a = int(input('Введите количество элементов в массиве: '))
f = []

for i in range(0, a, 1):
    d = int(input(f'Введите элемент массива {i}: '))
    f.append(d)
b = np.array(f)

def func(c):
    e = 1
    for j in range(0, a, 1):
        e *= b[j]
    x = e 
    return x 

print(func(b))
