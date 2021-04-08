n = int(input())
for i in range(1,n):
    d = 0
    w = i
    while w > 0 :
        w //= 10
        d += 1
    if i == i ** 2 % (10**d):
        print(i)
