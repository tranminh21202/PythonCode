def checkip(xau):
    tmp = ""
    dem = 0
    slso = 0
    for x in range(0,len(xau)):
        if xau[x].isdigit():
            tmp += xau[x]
        elif xau[x] == '.':
            if len(tmp) == 0:
                return False
            else:
                dem += 1
                if int(tmp) > 255 or dem > 3:
                    return False
                else:
                    slso += 1
                    tmp = ""
        else:
            return False
    if len(tmp) > 0:
        slso += 1
        if int(tmp) > 255 or slso != 4:
            return False
    if dem < 3:
        return False
    return True
t = int(input())
while t > 0:
    xau = input()
    if checkip(xau):
        print("YES")
    else:
        print("NO")
    t -= 1