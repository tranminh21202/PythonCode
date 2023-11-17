t = int(input())
while t > 0:
    xau = input()
    kq = ""
    if len(xau) <= 100:
        print(xau)
    else:
        tmp = ""
        dem = 0
        for x in range(0,len(xau)):
            if xau[x] == " ":
                tmp += xau[x]
                if dem + len(tmp) <= 100:
                    dem += len(tmp)
                    kq += tmp
                    tmp = ""
                else:
                    print(kq)
                    break
            else:
                tmp += xau[x]
    t -= 1