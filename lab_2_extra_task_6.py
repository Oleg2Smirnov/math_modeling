a = int(input('Введите год'))
b = int(input('Введите месяц'))
c = -776
d = 7

e = (a - c) // 4 + 1
f = (a - c) % 4
if b < d and f == 0:
    f += 4
    e -= 1
else:
    f += 1
print(f'OL {e}.{f}')