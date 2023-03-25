n = int(input())
ds = list(map(int,input().split()))
ok = True
while ok:
    ok = False
    i = 0
    while i < len(ds)-1:
        if (ds[i] + ds[i+1]) % 2 == 0:
            del ds[i]
            del ds[i]
            ok = True
        i += 1
print(len(ds))