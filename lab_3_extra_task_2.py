import numpy as np

a = np.zeros((1, 5))

for i in range(0, 4, 1):
    a[0, i] = int(input(f'Введите элемент массива {i}: '))
print(a)

d = np.array(a)
b = int(input('Введите значение элемента 4: '))
c = int(input('Введите позицию элемента 4 (0 < x < 6): '))

while c < 1 or c > 5:
    c = int(input('Введите позицию элемента 4 (0 < x < 6): '))

for i in range(c-1, 4, 1):
    a[0, i+1] = d[0, i]
a[0, c] = b

print(a)