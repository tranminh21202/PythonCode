t = int(input())
while t > 0:
    p,q = map(int,input().split())
    xau = input().split()
    if len(xau) == 2:
        x1 = xau[0]
        x2 = xau[1]
    else:
        x1 = xau[0]
        x2 = input()
    x1q = ""
    x1p = ""
    x2q = ""
    x2p = ""
    for x in range(0,len(x1)):
        if int(x1[x]) == p:
            x1q += str(q)
        else:
            x1q += x1[x]
    for x in range(0,len(x2)):
        if int(x2[x]) == p:
            x2q += str(q)
        else:
            x2q += x2[x]
    for x in range(0,len(x1)):
        if int(x1[x]) == q:
            x1p += str(p)
        else:
            x1p += x1[x]
    for x in range(0,len(x2)):
        if int(x2[x]) == q:
            x2p += str(p)
        else:
            x2p += x2[x]
    min = int(x1q) + int(x2q)
    max = int(x1p) + int(x2p)
    if min < max:
        print(min,max)
    else:
        print(max,min)
    t -= 1