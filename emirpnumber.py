import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def daoxau(xau):
    tmp = ""
    for x in range(0,len(xau)):
        tmp = xau[x] + tmp
    return tmp

t = int(input())
while t > 0:
    n = int(input())
    kq = []
    for x in range(13,n):
        xau = str(x)
        dao = int(daoxau(xau))
        if checknto(x) and checknto(dao) and x != dao and dao < n:
            if dao not in kq:
                kq.append(x)
                kq.append(dao)
    for x in kq:
        print(x,end=" ")
    print()
    t -= 1