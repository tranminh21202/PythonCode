import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def checkprime(xau):
    so = int(xau)
    if checknto(so) == False:
        return False
    dao = ""
    sum = 0
    for x in range(0,len(xau)):
        if checknto(int(xau[x])) == False:
            return False
        else:
            sum += int(xau[x])
            dao = xau[x] + dao
    sodao = int(dao)
    if checknto(sodao) == False or checknto(sum) == False:
        return False
    return True
t = int(input())
while t > 0:
    xau = input()
    if checkprime(xau):
        print("Yes")
    else:
        print("No")
    t -= 1