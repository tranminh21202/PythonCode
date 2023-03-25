t = int(input())
while t > 0:
    xau = input()
    min = 10e9
    tmp = ""
    for x in range(0,len(xau)):
        if xau[x].isdigit():
            tmp += xau[x]
        else:
            if len(tmp) > 0:
                so = int(tmp)
                if min > so:
                    min = so - 0
                    tmp = ""
                else:
                    tmp = ""
                    continue
            else:
                continue
    print(min)
    t -= 1