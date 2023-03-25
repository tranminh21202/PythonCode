t = int(input())
while t > 0:
    xau = input()
    kq = []
    tong = 0
    for x in range(0,len(xau)):
        if xau[x].isdigit():
            tong += int(xau[x])
        else:
            kq.append(xau[x])
    kq.sort()
    print("".join(kq),end="")
    print(tong)
    t -= 1