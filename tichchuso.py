def tichchuso(xau):
    tich = 1
    for x in range(0,len(xau)):
        if int(xau[x]) != 0:
            tich *= int(xau[x])
        else:
            continue
    return tich
t = int(input())
while t > 0:
    xau = input()
    print(tichchuso(xau))
    t -= 1