name = 'Smirnov Oleg Vladimirovich'
a = []
d = []

name = '_'.join(name)
print(name)

name = name.upper()

for symbol in name:
   a.append(ord(symbol))
print(a)

name = name.lower()
for symbol in name:
    d.append(ord(symbol))
print(d)

print(f'Сумма значений из списка с верхним регистром: {sum(a)}')
print(f'Сумма значений из списка с нижним регистром: {sum(d)}')
