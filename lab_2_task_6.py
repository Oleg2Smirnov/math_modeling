e = 1
while e < 10:
    print(e, 2*e, 3*e, 4*e, 5*e, 6*e, 7*e, 8*e, 9*e)
    e += 1

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(j*i, end=' ')
    print()
