def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)
n = int(input())
kq = list(map(int,input().split()))
kq.sort()
for x in range(0,len(kq)-1):
    for y in range(x+1,len(kq)):
        if ucln(kq[x],kq[y]) == 1:
            print(kq[x],end=" ")
            print(kq[y])
