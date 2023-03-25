t = int(input())
while t > 0:
    xau = input()
    tong = 0
    tich = 1
    for x in range(0,len(xau)):
        if x % 2 == 0:
            tong += int(xau[x])
        else:
            if int(xau[x]) != 0:
                tich *= int(xau[x])
            else:
                continue
    print(tong,end=" ")
    if tich != 1:
        print(tich)
    else:
        print(0)
    t -= 1