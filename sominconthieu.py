n = int(input())
ds = list(map(int,input().split()))
ok = False
ds.sort()
for x in range(0,n-1):
    if ds[x+1] != ds[x] + 1: 
        print(ds[x] + 1)
        ok = True
        break
    else:
        continue
if ok == False:
    print(ds[-1]+1)