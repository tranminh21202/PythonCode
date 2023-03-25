t = int(input())
while t > 0:
    n = int(input())
    ds = list(map(int,input().split()))
    ds.sort()
    dem = 0
    xhnn = 0
    tmp = 1
    for x in range(0,n-1):
        if ds[x] == ds[x+1]:
            tmp += 1
        else:
            if tmp > dem:
                dem = tmp
                xhnn = ds[x]
                tmp = 1
            else:
                tmp = 1
                continue
    if tmp > dem:
        dem = tmp
        xhnn = ds[n-1]
    if dem > int(n/2):
        print(xhnn)
    else:
        print("NO")
    t -= 1