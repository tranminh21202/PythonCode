import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def checkxau(xau):
    for x in range(0,len(xau)):
        if checknto(x):
            if checknto(int(xau[x])) == False:
                return False
        else:
            if checknto(int(xau[x])) == True:
                return False
    return True
t = int(input())
while t > 0:
    xau = input()
    if checkxau(xau):
        print("YES")
    else:
        print("NO")
    t -= 1