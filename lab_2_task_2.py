a = int(input('Первый член: '))
b = int(input('Знаменатель: '))
c = int(input('Количество членов: '))
d = c - 1
e = 1

print(a)
while a * b ** (c - 1) > a * (b * e) and d > e:
    print(a * (b ** e))
    e += 1
print(a * b ** (c - 1))




for i in range(c-1):
    a = a*b
    print(a)
