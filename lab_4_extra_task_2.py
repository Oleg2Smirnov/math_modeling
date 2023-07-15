n = int(input('Введите номер элемента: '))

def fib(n):
    a = [0, 1]
    for i in range(2, n, 1):
        b = a[i-1] + a[i-2]
        a.append(b)
    return a[n-1]

print(fib(n))
