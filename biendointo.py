import math
def checkngto(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def tang(n):
    dem=0
    while checkngto(n)==False:
        n+=1
        dem+=1
    return dem
def giam(n):
    dem=0
    while checkngto(n)==False:
        n-=1
        dem+=1
    return dem
n = int(input())
ds =list()
while True:
    ds += list(map(int,input().split()))
    if n == len(ds):
        break
ds2 = list()
for i in ds:
    if checkngto(i) == False:
        ds2.append(i)
buoc = 0
for i in ds2:
    buoc = max(buoc,min(tang(i),giam(i)))
print(buoc)