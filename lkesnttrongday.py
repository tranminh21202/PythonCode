import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

n = int(input())
ds = list(map(int,input().split()))
tmp = []
for x in ds:
    if x not in tmp:
        tmp.append(x)
for x in tmp:
    if checknto(x):
        print(x,end=" ")
        print(ds.count(x))
