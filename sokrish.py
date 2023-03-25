def giaithua(n):
    tich = 1
    for x in range(1,n+1):
        tich *= x
    return tich

def checkkrish(xau):
    tong = 0
    for x in range(0,len(xau)):
        tong += giaithua(int(xau[x]))
    if tong == int(xau):
        return True
    else:
        return False
t = int(input())
while t > 0:
    xau = input()
    if checkkrish(xau):
        print("Yes")
    else:
        print("No")
    t -= 1