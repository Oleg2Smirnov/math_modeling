print('A B C D F')
for A in range(0, 2, 1):
    for B in range(0, 2, 1):
        for C in range(0, 2, 1):
            for D in range(0, 2, 1):
                F = (not(A) and B) or (not(C) and D)
                print(A, B, C, D, int(F))
