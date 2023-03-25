def tinhfibo(n):
    listfibo = []
    f1 = 1
    f2 = 1
    listfibo.append(f1)
    listfibo.append(f2)
    for x in range(1,n):
        fn = f1 + f2
        listfibo.append(fn)
        f1 = f2
        f2 = fn
    return listfibo

t = int(input())
while t > 0:
    a,b = map(int,input().split())
    kq = tinhfibo(b)
    for x in range(a-1,b):
        print(kq[x],end=" ")
    print()
    t -= 1