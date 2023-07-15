import numpy as np

a = int(input('Введите 1 для нахождения площади круга; 2 для нахождения площади треугольника; 3 для нахождения площади прямоугольника: '))

def func_1(R):
    S = np.pi * R ** 2
    return S

def func_2(b, h):
    S = b * h / 2
    return S

def func_3(b, c):
    S = b * c
    return S

if a == 1: 
    R = float(input('Введите радиус окружности: '))
    print(func_1(R))
elif a == 2:
    b = float(input('Введите длину основания треугольника: '))
    h = float(input('Введите длину высоты, проведённой к основанию: '))
    print(func_2(b, h))
else:
    b = float(input('Введите длину одной стороны прямоугольника: '))
    c = float(input('Введите длину другой стороны прямоугольника: '))
    print(func_3(b, c))
