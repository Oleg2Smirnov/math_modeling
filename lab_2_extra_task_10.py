import random 
numbers = []
for i in range(20):
    numbers.append(random.randint(-100,100))
print(numbers)
a = numbers[0]
b = a
e = a

for i in range(0, 19, 1):
    a = numbers[i + 1] * a
print(f'Произведение всех чисел: {a}')

for i in range(0, 19, 1):
    b = numbers[i + 1] + b
print(f'Сумма всех чисел: {b}')

c = b / 20
print(f'Среднее арифметическое всех чисел: {c}')

d = (a ** 2) ** (1 / 40)
print(f'Среднее геометрическое всех чисел: {d}')

for i in range(0, 19, 1):
    if e < numbers[i + 1]:
        e = numbers[i + 1]
    else:
        e = e
print(f'Максимум: {e}')

for i in range(0, 19, 1):
    if e > numbers[i + 1]:
        e = numbers[i + 1]
    else:
        e = e
print(f'Минимум: {e}')