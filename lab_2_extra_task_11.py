x = int(input('Сумма вклада: '))
y = int(input('Процент вклада: '))
n = int(input('Количество лет: '))
e = 0

while e < n:
    x = x + x * y / 100
    e += 1
print(x)