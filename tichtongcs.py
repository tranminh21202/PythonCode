t = int(input())
while t > 0:
    xau = input()
    tich = 1
    tong = 0
    for x in range(0,len(xau)):
        if x % 2 == 0:
            if int(xau[x]) != 0:
                tich *= int(xau[x])
            else:
                continue
        else:
            tong += int(xau[x])
    print(tich,end=" ")
    print(tong)
    t -= 1