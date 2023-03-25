import itertools
t = int(input())
while t > 0:
    n = int(input())
    kq = list()
    for x in range(1,n+1):
        kq.append(x)
    kq.reverse()
    ds = itertools.permutations(kq,n)
    dem = 1
    for x in range(1,n+1):
        dem *= x
    print(dem)
    for i in ds:
        for j in range(0,n):
            print(i[j],end="")
        print(" ",end="")
    print()
    t -= 1