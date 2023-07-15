g = 10 
M = 5.97237 * 10 ** 24
G = 6.67408 * 10 ** (-11) 

m = float(input('Введите массу тела: '))
h = float(input('Введите высоту тела: '))
v = float(input('Введите скорость тела на высоте h: '))

def func(a, b, c):
    k = (a * c ** 2) / 2
    U = a * g * b
    E = k + U
    return E

print(func(m, h, v))
