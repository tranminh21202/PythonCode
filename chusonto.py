import math
def checknto(n):
    if n < 2: return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True
t = int(input())
while t > 0:
    xau = input()
    demnto = 0
    demknto = 0
    for x in range(0,len(xau)):
        if checknto(int(xau[x])):
            demnto += 1
        else:
            demknto += 1
    if checknto(len(xau)) == False or demknto >= demnto:
        print("NO")
    else:
        print("YES")
    t -= 1