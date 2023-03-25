def checkxenke(xau):
    if len(xau) % 2 == 0:
        return False
    if int(xau[0]) == int(xau[1]):
        return False
    for x in range(0,len(xau)-2,2):
        if int(xau[x]) != int(xau[x+2]):
            return False
    return True
t = int(input())
while t > 0:
    xau = input()
    if checkxenke(xau):
        print("YES")
    else:
        print("NO")
    t -= 1