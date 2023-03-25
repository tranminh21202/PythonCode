t = int(input())
P = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while t > 0:
    xau = input().upper()
    dao = ""
    ok = True
    for x in xau:
        dao = x + dao
    for x in range(0,len(xau)-1):
        s1 = P.index(xau[x])
        s3 = P.index(xau[x+1])
        s2 = P.index(dao[x])
        s4 = P.index(dao[x+1])
        if abs(s1-s3) != abs(s2-s4):
            print("NO")
            ok = False
            break
    if ok:
        print("YES")
    t -= 1