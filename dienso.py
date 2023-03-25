t = int(input())
while t > 0:
    n = int(input())
    ds = list(map(int,input().split()))
    kq = []
    for x in ds:
        if x not in kq:
            kq.append(x)
    kq.sort()
    tmp = kq[-1] - kq[0] + 1
    print(tmp-len(kq))
    t -= 1