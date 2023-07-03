a = int(input())
b = int(input())

if a == 0:
    print('Делится; частное = 0')
elif b == 0:
    print('не делится; частное = бесконечность')
else:
    if a / b == a // b:
        print('Делится;', 'частное =', a / b)
    else:
        print('Не делится;', 'частное =', a % b)
