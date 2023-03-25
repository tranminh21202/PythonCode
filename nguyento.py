import math
def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)

def checknt(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    k = 0
    for x in range(1,n):
        if ucln(x,n) == 1:
            k += 1
    if checknt(k):
        print("YES")
    else:
        print("NO")
    t -= 1
    


