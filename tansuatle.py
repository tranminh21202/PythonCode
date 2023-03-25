t = int(input())
while t > 0:
    n = int(input())
    ds = list(map(int,input().split()))
    ds.sort()
    i = 0
    while len(ds) > 1:
        if ds[i] == ds[i+1]:
            ds.pop(i)
            ds.pop(i)
        else:
            i+=1
    for x in ds:
        print(x)
    t -= 1