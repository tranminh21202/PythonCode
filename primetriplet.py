import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

def sangnt(n):
    ds = [1 for i in range(n+1)]
    ds[0] = ds[1] = 0
    p = 2
    while p <= int(math.sqrt(n)):
        if checknto(p):
            for i in range(p**2,n+1,p):
                ds[i] = 0
        p += 1
    return ds

t = int(input())
while t > 0:
    n = int(input())
    dem = 0
    kq = sangnt(n)
    for i in range(2,len(kq)-6):
        if kq[i] == 1 and kq[i+2] == 1 and kq[i+6] == 1:
            dem += 1
        elif kq[i] == 1 and kq[i+4] == 1 and kq[i+6] == 1:
            dem += 1
    print(dem)
    t -= 1