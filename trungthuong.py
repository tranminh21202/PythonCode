t = int(input())
while t > 0:
    n = int(input())
    ds = []
    dem = 0
    tmp = 1
    min = 0
    while n > 0:
        ran = int(input())
        ds.append(ran)
        n -= 1
    ds.sort()
    for x in range(0,len(ds)-1):
        if ds[x] == ds[x+1]:
            tmp += 1
        else:
            if tmp > dem:
                dem = tmp
                tmp = 1
                min = ds[x]
            else:
                tmp = 1
    if tmp > dem:
        dem = tmp
        min = ds[len(ds)-1]
    print(min)
    t -= 1