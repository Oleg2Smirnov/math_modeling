e = 1
while e < 10:
    print(e, 2*e, 3*e, 4*e, 5*e, 6*e, 7*e, 8*e, 9*e)
    e += 1

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(j*i, end=' ')
    print()

a = ' '
b = int(input('Введите количество строк: '))
c = int(input('Введите количество столбцов: '))
for i in range(1, b + 1, 1):
    for j in range(1, c + 1, 1):
        d = len(str(i*j))
        e = len(str(j*b))
        print(i*j, end=a * (e - d + 1))
    print()
