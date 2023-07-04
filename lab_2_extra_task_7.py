x = int(input('Координата x:'))
y = int(input('Координата y:'))
r = int(input('Радиус круга r:'))

if x**2 + y**2 <= r**2:
    print('Принадлежит')
else:
    print('Не принадлежит')