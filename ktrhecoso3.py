t = int(input())
while t > 0:
    xau = input()
    ok = True
    for x in range(0,len(xau)):
        if xau[x].isdigit():
            if int(xau[x]) != 0 and int(xau[x]) != 1 and int(xau[x]) != 2:
                print("NO")
                ok = False
                break
        else:
            continue
    if ok == True:
        print("YES")
    t -= 1