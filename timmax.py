t = int(input())
while t > 0:
    xau = input()
    max = 0
    tmp = ""
    for x in range(0,len(xau)):
        if xau[x].isdigit():
            tmp += xau[x]
        else:
            if len(tmp) > 0:
                if max < int(tmp):
                    max = int(tmp)
                    tmp = ""
                else:
                    tmp = ""
            else:
                continue
    if tmp.isdigit():
        if max < int(tmp):
            max = int(tmp)
    print(max)
    t -= 1