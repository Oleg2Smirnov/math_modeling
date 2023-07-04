a = int(input())
b = []
d = str()
f = 2
e = 1
g= -1

while f <= a:
    if a / f == a // f and a // f != 1:
        b.append(f'{f} * ')
        a /= f
        g += 1
    elif a / f != a // f:
        f += 1
    else:
        a /= f
        f += 1
while e - 1 < g + 1:
    c = b[e - 1]
    d += c
    e += 1
print(f'{d}{f - 1}')