n = int(input())
tmp = 0
ds = []
ok = True
while ok:
    tm = [int(x) for x in input().split()]
    for x in tm:
        ds.append(x)
        tmp += 1
        if tmp == n:
            ok = False
            break
    if ok == False:
        break
chan = []
le = []
for x in ds:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
chan.sort()
le.sort(reverse=True)
kq = []
i = 0
j = 0
for x in ds:
    if x % 2 == 0:
        kq.append(chan[i])
        i += 1
    else:
        kq.append(le[j])
        j += 1
for x in kq:
    print(x,end=" ")
print()