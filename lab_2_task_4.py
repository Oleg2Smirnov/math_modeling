#a = int(input('Введите число элементов'))
#b = 1
#c = [1]
#d = 1
#e = 2
#
#if a < 1:
#    print('Введя число, которое больше 0 дурак')
#elif a == 1:
#    print(c)
#else:
#    c.append(d)
#while a - e > 0:
#    c.append((c[d] + c[d-1]))
#    d += 1
#    e += 1
#print(c)


a = int(input('Введите число элементов: '))
b = [1, 1]

for i in range(0, a - 2, 1):
    c = b[i] + b[ i + 1]
    b.append(c)
print(b)

