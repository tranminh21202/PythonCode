import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

n = int(input())
ds = list(map(int,input().split()))
dsnto = []
for x in ds:
    if checknto(x):
        dsnto.append(x)
dsnto.sort()
i = 0
for x in ds:
    if checknto(x) == False:
        print(x,end=" ")
    else:
        print(dsnto[i],end=" ")
        i += 1
