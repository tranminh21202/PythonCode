import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True
t = int(input())
while t > 0:
    xau = input()
    so = int(xau[-4:])
    if checknto(so):
        print("YES")
    else:
        print("NO")
    t -= 1