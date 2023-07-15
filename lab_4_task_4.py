print('a < x < b')
N = int(input('Введите количество точек функции: '))
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))

def func(a, b, c):
    for i in range(0, c, 1):
        d = float(input(f'Введите значение x{i+1}: '))
        while d < a or d > b:
            d = float(input(f'Введите значение x{i+1} (a < x < b): '))
        x = d ** 2
        print(f'y = {x}')
        
print(func(a, b, N))
