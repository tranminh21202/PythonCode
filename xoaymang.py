t = int(input())
while t > 0:
    n,d = map(int,input().split())
    ds = list(map(int,input().split()))
    tmp = ds[:d]
    kq = ds[d:]
    kq.extend(tmp)
    for x in kq:
        print(x,end=" ")
    print()
    t -= 1