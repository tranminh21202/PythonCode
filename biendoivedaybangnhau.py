n = int(input())
ds= list()
kq = 10**9
gtri = -1
ds = list(map(int,input().split()))
for i in range(n):
    buoc = 0
    for j in range(n):
        buoc += abs(ds[j]-ds[i])
    if buoc < kq:
        kq = buoc
        gtri = ds[i]
print(kq,gtri)