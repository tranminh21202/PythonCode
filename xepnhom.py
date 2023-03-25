t = int(input())
while t > 0:
    n,k = map(int,input().split())
    dso = list(map(int,input().split()))
    dem = 0
    while len(dso) >= k:
        dso.sort(reverse=True)
        tmp = 0
        x = 0
        ok = True
        while ok:
            if dso[x] != 0:
                tmp += 1
                dso[x] -= 1
            elif dso[x] == 0:
                dso.pop(x)
            x += 1  
            if tmp == k:
                ok = False 
                dem += 1
        print(dem)
    t -= 1
