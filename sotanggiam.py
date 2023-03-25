t = int(input())
while t > 0:
    xau = input()
    ok = False
    tmp = 0
    if len(xau) < 3:
        print("NO")
    else:
        for x in range(0,len(xau)-1):
            if int(xau[x]) > int(xau[x+1]):
                tmp = x + 1
                break
            elif int(xau[x]) == int(xau[x+1]):
                print("NO")
                ok = True
                break
        if ok == False:
            for i in range(tmp,len(xau)-1):
                if int(xau[i]) <= int(xau[i+1]):
                    print("NO")
                    ok = True
                    break
        if ok == False:
            print("YES")
    t -= 1