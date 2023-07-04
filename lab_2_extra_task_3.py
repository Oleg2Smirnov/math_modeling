# a = int(input())
# b = []
# e = 1
# f = 1
# g = 10

# while a > 1:
#     c = a % 10
#     b.append(c)
#     a //= 10
#     f += 1
# b.append(0)
# d = b[0]
# while f > 1:
#     d = d * 10 + b[e]
#     e += 1
#     f -= 1 
# print(d // 10)


a = input()
for i in range(0, len(a)):
    print(a[-i-1], end='')
