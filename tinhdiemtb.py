n = int(input())
ds = list(map(float,input().split()))
ds.sort()
tong = 0
dem = 2
for x in range(1,len(ds)-1):
    if ds[x] == ds[0] or ds[x] == ds[-1]:
        dem += 1
        continue
    else:
        tong += ds[x]
tb = tong / (len(ds)-dem)
print(f"{tb:.2f}")