a = int(input('Введите количество элементов в массиве: '))
b = []

for i in range(0, a, 1):
    d = float(input(f'Введите элемент массива {i}: '))
    b.append(d)

def func(c):
    e = 0
    for i in range(0, len(c), 1):
        e += b[i]
    x = e / len(c)
    return x 

print(func(b))
