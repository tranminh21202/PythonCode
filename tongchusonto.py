import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True
def checktong(xau):
    sum = 0
    for x in range(0,len(xau)):
        sum += int(xau[x])
    if checknto(sum):
        return True
    else:
        return False
t = int(input())
while t > 0:
    xau = input()
    if checktong(xau):
        print("YES")
    else:
        print("NO")
    t -= 1