t = int(input())
kq = []
while t > 0:
    ds = list(input().split())
    kq.append(len(ds))
    t -= 1
k = []
a = []
ok = 0
for x in kq:
    if len(a) == 0 and x == 6:
        k.append(1)
    a.append(x)
    if len(a) > 1 and x == 6 and a[-2] == 7:
        k.append(1)
    if x == 7:
        ok += 1
    if ok == 4:
        k.append(2)
        ok = 0
print(len(k))
for x in k:
    print(x)
