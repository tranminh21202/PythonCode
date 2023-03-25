import math
def checksnto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True
t = int(input())
while t > 0:
    xau = input()
    so = xau[-4:]
    n = int(so)
    if checksnto(n) == True:
        print("YES")
    else:
        print("NO")
    t -= 1