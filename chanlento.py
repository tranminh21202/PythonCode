import math
def checknto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def checkchanle(xau):
    sum = 0
    for x in range(0,len(xau)):
        sum += int(xau[x])
        if x % 2 == 0:
            if int(xau[x]) % 2 != 0:
                return False
            else:
                continue
        else:
            if int(xau[x]) % 2 == 0:
                return False
            else:
                continue
    if checknto(sum) == False:
        return False
    else:
        return True
    return True
t = int(input())
while t > 0:
    xau = input()
    if checkchanle(xau):
        print("YES")
    else:
        print("NO")
    t -= 1