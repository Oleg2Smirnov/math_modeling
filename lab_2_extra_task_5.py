a = int(input())
b = 2
c = 2
d = []
e = 2

while b <= a:
    if b / c == b // c and b != c:
        e += c
        c += 1
        if b == e:
            d.append(b)
            b += 1
            e = 1
            c = 2
        else:
            f = 1
    elif b == c:
        b += 1
        e = 1
        c = 2
    else:
        c += 1
print(d)
