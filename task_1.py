import numpy as np

x = float(input('Введите значение x от 0 до 100: '))
while x < 0 or x > 100:
    x = float(input('Введите значение x от 0 до 100: '))
y = float(input('Введите значение y от 0 до 100: '))
while y < 0 or y > 100:
    y = float(input('Введите значение y от 0 до 100: '))

if y == 0:
    for i in range(0, 100, 1):
        x1 = i
        if x-x1 < 1 and x-x1 > -1:
            print('Yes')
            break
        else:
            x -= 1
            if x-x1 < 1 and x-x1 > -1:
                print('Yes')
                break
    if i == 99:
        if x-x1 < 1 and x-x1 > -1:
            print('Yes')
        else:
            x -= 1
            if x-x1 < 1 and x-x1 > -1:
                print('Yes')
            else:
                x1 = 100
                if x-x1 < 1 and x-x1 > -1:
                    print('Yes')
                else:
                    print('No')              

else:
    for i in range(0, 100, 1):
        x1 = i
        if (x-x1)**2 + y**2 < 1:
            print('Yes')
            break
        if (x-x1)**2 + y**2 >= 1:
            alpha = np.arctan((x1-x)/y)
            x = x + np.sin(alpha) * 1
            y = y - np.cos(alpha) * 1 
            if (x-x1)**2 + y**2 <= 1:
                print('Yes')
                break
        if i == 99:
            if (x-x1)**2 + y**2 < 1:
                print('Yes')
                break
            else:
                x3 = 100
                if (x-x3)**2 + y**2 < 1:
                    print('Yes')
                else:
                    print('No')
                    




