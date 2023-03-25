t = int(input())
def checktong(xktu):
    sum = 0
    for x in range(0,len(xktu)):
        sum += int(xktu[x])
    if sum % 10 == 0:
        return True
    else:
        return False
while t > 0:
    xau = input()
    ok = True
    if checktong(xau) == False:
        print("NO")
        ok = False
    else:
        for x in range(0,len(xau)-1):
            a = int(xau[x])
            b = int(xau[x+1])
            if a-b!=2 and b-a!=2:
                print("NO")
                ok = False
                break
    if ok == True:
        print("YES")
    t -= 1