import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

def lke(n):
    ds = []
    while n > 0:
        for x in range(2,100000):
            if checknto(x):
                ds.append(x)
                n -= 1
    return ds

n,x = map(int,input().split())
nt = lke(n)
kq = []
kq.append(x)
i = 0
while i < n:
    tmp = nt[i] + kq[i]
    kq.append(tmp)
    i += 1
for x in kq:
    print(x,end=" ")
print()