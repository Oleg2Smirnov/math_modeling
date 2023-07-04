x = int(input())
if x > 0:
    y = 2*x - 10
elif x == 0:
    y = 0
else:
    if x < 0:
        y = 2*(-x) - 1
    else:
        y = 2*x - 1
print(y)