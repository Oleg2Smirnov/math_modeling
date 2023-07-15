a = float(input('a = '))
n = int(input('n = '))

def func(a, n):
    b = 1
    for i in range(0, n, 1):
        b *= a
    return b

print(func(a, n))
