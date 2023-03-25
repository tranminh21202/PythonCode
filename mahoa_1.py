t = int(input())
while t>0:
    xau = input()
    dem = 1
    for x in range(1,len(xau)):
        if xau[x-1] == xau[x]:
            dem += 1
        else:
            print(f"{dem}{xau[x-1]}", end='')
            dem = 1
    if xau[len(xau)-1] == xau[len(xau)-2]:
        print(f"{dem}{xau[len(xau)-1]}")
    else:
        print(f"{1}{xau[len(xau)-1]}")
    t = t - 1