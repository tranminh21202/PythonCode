t = int(input())
while t > 0:
    so = input()
    ok = True
    for x in range(0,len(so)):
        i = int(so[x])
        if i != 4 and i != 7:
            ok = False
            break
    if ok == True:
        print("YES")
    else:
        print("NO")
    t -= 1