import math
def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)

def checknt(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

t = int(input())
while t > 0:
    xau = input()
    a = xau.split()
    x1,x2 = map(int,a)
    uc = int(ucln(x1,x2))
    sum = 0
    while uc > 0:
        sum += uc % 10
        uc = uc // 10
    if checknt(sum):
        print("YES")
    else:
        print("NO")
    t -= 1
