a = int(input())
b = int(input())
c = int(input())

if a > b + c or b > a + c or c > a + b:
    print('Такого треугольника нет')
else:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')