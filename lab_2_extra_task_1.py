a = int(input('Коэффициент a: '))
b = int(input('Коэффициент b: '))
c = int(input('Коэффициент c: '))
D = b ** 2 - 4 * a * c 

if D < 0:
    print('Корней нет')
elif D == 0:
    x = - b / 2 / a
    print(f'Корень уравнения: x = {x}')
else:
    x = (- b + D ** 0.5) / 2 / a
    y = (- b - D ** 0.5) / 2 / a
    print(f'Корни уравнения: x₁ = {x} ; x₂ = {y}')