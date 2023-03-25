n = int(input())
ds = list(map(int,input().split()))
dem = 0
for x in range(0,len(ds)-1):
    for y in range(x+1,len(ds)):
        if ds[x] > ds[y]:
            dem += 1
print(dem)