t = int(input())
while t > 0:
    xau = input()
    ok = True
    for x in range(0,len(xau)-1):
        so1 = xau[x]
        so2 = xau[x+1]
        if so2 < so1:
            ok = False
            break
    if ok == True:
        print("YES")
    else:
        print("NO")
    t -= 1
